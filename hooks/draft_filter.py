"""
Hook MkDocs para filtrar páginas por status del front matter.

Comportamiento:
- DRAFT_MODE=true: Muestra todo el contenido + banners visuales para drafts
- DRAFT_MODE=false: Solo muestra páginas con status=published
                    Enlaces a páginas draft se convierten en "texto (próximamente)"
                    Bloques <!-- draft:start -->...<!-- draft:end --> se eliminan

Uso:
    export DRAFT_MODE=true   # desarrollo local
    export DRAFT_MODE=false  # producción

Bloques draft inline:
    <!-- draft:start -->
    Contenido en desarrollo que solo aparece en DRAFT_MODE=true
    <!-- draft:end -->
"""
import os
import re
import logging
import yaml

log = logging.getLogger('mkdocs.hooks.draft_filter')

DRAFT_MODE = os.environ.get('DRAFT_MODE', 'false').lower() == 'true'
DEFAULT_STATUS = 'draft'

# Cache de archivos published para filtrar navegación y enlaces
_published_files = set()
_docs_dir = None


def on_files(files, config):
    """Filtra archivos según su status en el front matter."""
    global _published_files, _docs_dir
    _published_files = set()
    _docs_dir = config['docs_dir']

    if DRAFT_MODE:
        log.info("DRAFT_MODE activo: mostrando todo el contenido")
        for file in files:
            if file.src_path.endswith('.md'):
                _published_files.add(file.src_path)
        return files

    from mkdocs.structure.files import Files
    filtered = []

    for file in files:
        if not file.src_path.endswith('.md'):
            filtered.append(file)
            continue

        status = _get_status(file, config)
        if status == 'published':
            filtered.append(file)
            _published_files.add(file.src_path)
        else:
            log.debug(f"Excluyendo archivo: {file.src_path} (status: {status})")

    return Files(filtered)


def on_nav(nav, config, files):
    """Filtra la navegación para excluir páginas draft."""
    if DRAFT_MODE:
        return nav

    # Filtrar items de navegación recursivamente
    _filter_nav_items(nav.items, config['docs_dir'])
    return nav


def _filter_nav_items(items, docs_dir):
    """Filtra recursivamente los items de navegación in-place."""
    to_remove = []

    for item in items:
        if hasattr(item, 'file') and item.file:
            # Es una página
            if item.file.src_path not in _published_files:
                log.debug(f"Excluyendo nav: {item.file.src_path}")
                to_remove.append(item)
        elif hasattr(item, 'children') and item.children:
            # Es una sección con hijos
            _filter_nav_items(item.children, docs_dir)
            # Si quedó vacía, marcar para eliminar
            if not item.children:
                log.debug(f"Excluyendo sección vacía: {item.title}")
                to_remove.append(item)

    for item in to_remove:
        items.remove(item)


def _normalize_path(page_path):
    """Normaliza un path de página a formato src_path."""
    if not page_path.endswith('.md'):
        # Puede ser un directorio (e.g., "installation/")
        # MkDocs lo convierte a installation/index.md
        if page_path.endswith('/'):
            return page_path + 'index.md'
        else:
            return page_path + '/index.md'
    return page_path


def _get_status_from_path(full_path):
    """Extrae el status del front matter dado un path completo."""
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                fm = yaml.safe_load(content[3:end])
                if fm and 'status' in fm:
                    return fm['status']

        return DEFAULT_STATUS
    except Exception as e:
        log.warning(f"Error leyendo {full_path}: {e}")
        return DEFAULT_STATUS


def on_page_markdown(markdown, page, config, files):
    """
    En DRAFT_MODE: Elimina marcadores draft (mantiene contenido) y añade banner.
    En producción: Elimina bloques draft inline y convierte enlaces a páginas draft.
    """
    if DRAFT_MODE:
        markdown = _strip_draft_markers(markdown)
        return _add_draft_banner(markdown, page)
    else:
        markdown = _remove_draft_blocks(markdown)
        return _convert_draft_links(markdown, page, config)


def _add_draft_banner(markdown, page):
    """Añade banner visual para drafts en modo preview."""
    status = page.meta.get('status', DEFAULT_STATUS)

    if status == 'draft':
        banner = '''!!! warning "BORRADOR"
    Este documento está en desarrollo y **no aparecerá** en la documentación pública.

'''
        return banner + markdown

    elif status == 'review':
        banner = '''!!! info "EN REVISIÓN"
    Este documento está completo pero pendiente de aprobación.

'''
        return banner + markdown

    return markdown


def _strip_draft_markers(markdown):
    """Elimina solo los marcadores <!-- draft:start/end --> manteniendo el contenido."""
    markdown = re.sub(r'<!--\s*draft:start\s*-->\n?', '', markdown)
    markdown = re.sub(r'\n?<!--\s*draft:end\s*-->', '', markdown)
    return markdown


def _remove_draft_blocks(markdown):
    """Elimina bloques <!-- draft:start -->...<!-- draft:end --> del markdown."""
    # Usar función de reemplazo para preservar saltos de línea solo cuando existen
    pattern = re.compile(
        r'(\n?)<!--\s*draft:start\s*-->.*?<!--\s*draft:end\s*-->(\n?)',
        re.DOTALL
    )

    def replacer(match):
        before_newline = match.group(1)
        after_newline = match.group(2)
        # Si había salto de línea antes Y después, dejar solo uno
        if before_newline and after_newline:
            return '\n'
        # Si no había saltos (inline), no añadir nada
        return ''

    result = pattern.sub(replacer, markdown)
    # Limpiar líneas vacías múltiples (más de 2 seguidas)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result


def _convert_draft_links(markdown, page, config):
    """Convierte enlaces a páginas draft en texto con (próximamente)."""
    docs_dir = config['docs_dir']
    page_dir = os.path.dirname(page.file.src_path)

    # Patrón para enlaces markdown con posible negrita externa:
    # **[texto](url)** o [texto](url) o [**texto**](url)
    link_pattern = re.compile(r'(\*\*)?\[([^\]]+)\]\(([^)]+)\)(\*\*)?')

    def replace_link(match):
        bold_before = match.group(1) or ''
        link_text = match.group(2)
        link_url = match.group(3)
        bold_after = match.group(4) or ''

        # Ignorar enlaces externos, anclas y mailto
        if link_url.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)

        # Resolver path relativo
        resolved_path = _resolve_link_path(link_url, page_dir)

        # Verificar si está publicado
        if _is_link_published(resolved_path, docs_dir):
            return match.group(0)  # Mantener enlace original

        # Convertir a texto con (próximamente)
        log.debug(f"Convirtiendo enlace draft: [{link_text}]({link_url}) en página {page.file.src_path}")

        # Eliminar negritas del texto si las tiene (evitar duplicados)
        clean_text = re.sub(r'^\*+|\*+$', '', link_text)
        return f'**{clean_text}** *(próximamente)*'

    return link_pattern.sub(replace_link, markdown)


def _resolve_link_path(link_url, page_dir):
    """Resuelve un enlace relativo a un path absoluto desde docs_dir."""
    # Quitar anclas
    if '#' in link_url:
        link_url = link_url.split('#')[0]

    if not link_url:
        return None

    # Si es path absoluto (empieza con /), quitar el /
    if link_url.startswith('/'):
        return link_url[1:]

    # Resolver path relativo
    if page_dir:
        resolved = os.path.normpath(os.path.join(page_dir, link_url))
    else:
        resolved = os.path.normpath(link_url)

    # Si el path escapa de docs_dir, es inválido
    if resolved.startswith('..'):
        log.debug(f"Enlace escapa de docs_dir: {link_url} -> {resolved}")
        return None

    return resolved


def _is_link_published(link_path, docs_dir):
    """Verifica si el destino de un enlace está publicado."""
    if not link_path:
        return True  # Enlace vacío o ancla, mantener

    normalized = _normalize_path(link_path)

    # Verificar en cache
    if normalized in _published_files:
        return True

    # Verificar archivo directamente
    full_path = os.path.join(docs_dir, normalized)
    if os.path.exists(full_path):
        status = _get_status_from_path(full_path)
        return status == 'published'

    # Si el archivo no existe, marcarlo como "próximamente"
    # (es contenido planificado pero no creado aún)
    log.debug(f"Archivo no encontrado, marcando como próximamente: {normalized}")
    return False


def _get_status(file, config):
    """Extrae el status del front matter de un archivo."""
    try:
        path = os.path.join(config['docs_dir'], file.src_path)
        return _get_status_from_path(path)
    except Exception as e:
        log.warning(f"Error leyendo {file.src_path}: {e}")
        return DEFAULT_STATUS
