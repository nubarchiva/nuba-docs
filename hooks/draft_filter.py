"""
Hook MkDocs para filtrar páginas por status del front matter.

Comportamiento:
- DRAFT_MODE=true: Muestra todo el contenido + banners visuales para drafts
- DRAFT_MODE=false: Solo muestra páginas con status=published

Uso:
    export DRAFT_MODE=true   # desarrollo local
    export DRAFT_MODE=false  # producción
"""
import os
import logging

log = logging.getLogger('mkdocs.hooks.draft_filter')

DRAFT_MODE = os.environ.get('DRAFT_MODE', 'false').lower() == 'true'
DEFAULT_STATUS = 'draft'


def on_files(files, config):
    """Filtra archivos según su status en el front matter."""
    if DRAFT_MODE:
        log.info("DRAFT_MODE activo: mostrando todo el contenido")
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
        else:
            log.info(f"Excluyendo: {file.src_path} (status: {status})")

    return Files(filtered)


def on_page_markdown(markdown, page, config, files):
    """Añade banner visual para drafts en modo preview."""
    if not DRAFT_MODE:
        return markdown

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


def _get_status(file, config):
    """Extrae el status del front matter de un archivo."""
    import yaml
    try:
        path = os.path.join(config['docs_dir'], file.src_path)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                fm = yaml.safe_load(content[3:end])
                if fm and 'status' in fm:
                    return fm['status']

        return DEFAULT_STATUS
    except Exception as e:
        log.warning(f"Error leyendo {file.src_path}: {e}")
        return DEFAULT_STATUS
