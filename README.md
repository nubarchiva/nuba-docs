# Manual de Usuario nubarchiva

[![Deploy Documentation](https://github.com/tu-org/nubarchiva-docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/tu-org/nubarchiva-docs/actions/workflows/deploy.yml)

Documentación oficial para usuarios de **nubarchiva**, el sistema de gestión archivística.

## 📖 Ver la Documentación

La documentación está publicada en: **[https://docs.nubarchiva.org](https://docs.nubarchiva.org)**

## 🏗️ Estructura del Proyecto

```
nubarchiva-docs/
├── docs/                       # Contenido de la documentación
│   ├── index.md               # Página de inicio
│   ├── installation/          # Guía de instalación
│   ├── getting-started/       # Primeros pasos
│   ├── user-guide/            # Guía de usuario
│   ├── admin-guide/           # Guía de administración
│   ├── customization/         # Personalización
│   ├── changelog/             # Historial de versiones
│   └── assets/                # Recursos (imágenes, videos)
├── hooks/                      # Hooks de MkDocs
│   └── draft_filter.py        # Filtro de contenido draft/published
├── scripts/                    # Scripts de utilidad
│   ├── add-frontmatter.py     # Añadir front matter a archivos
│   └── build-public.sh        # Build de producción
├── mkdocs.yml                 # Configuración de MkDocs
├── serve.sh                   # Script de desarrollo local
└── .github/workflows/         # CI/CD con GitHub Actions
```

## 🚀 Desarrollo Local

### Prerrequisitos

- Python 3.11 o superior
- pip

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-org/nubarchiva-docs.git
cd nubarchiva-docs
```

2. Crea un entorno virtual de Python (recomendado):

```bash
python3 -m venv venv
```

3. Activa el entorno virtual:

**En macOS/Linux:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\Scripts\activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

### Servidor de Desarrollo

**Opción 1: Script automático (recomendado en macOS/Linux)**

```bash
./serve.sh
```

Este script se encarga de:
- Crear el entorno virtual si no existe
- Instalar dependencias si es necesario
- Activar el entorno virtual
- Iniciar el servidor

**Opción 2: Manual**

```bash
# Asegúrate de tener el entorno virtual activado
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate     # Windows

# Inicia el servidor
mkdocs serve
```

La documentación estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Los cambios en los archivos se reflejarán automáticamente en el navegador.

### Construcción

Para generar la versión estática:

```bash
# Asegúrate de tener el entorno virtual activado
source venv/bin/activate  # macOS/Linux

mkdocs build
```

Los archivos HTML se generarán en el directorio `site/`.

## 📋 Sistema de Publicación (Draft/Published)

Este proyecto implementa un sistema de publicación incremental que permite trabajar con contenido en diferentes estados sin publicar borradores.

### Estados del Contenido

Cada archivo `.md` debe tener un front matter YAML con el campo `status`:

```yaml
---
status: draft      # Borrador - en desarrollo
---

# Mi página
```

**Estados disponibles:**

| Estado      | Descripción             | Producción | Preview                     |
|-------------|-------------------------|------------|-----------------------------|
| `draft`     | Contenido en desarrollo | Excluido   | Visible con banner amarillo |
| `review`    | Pendiente de revisión   | Excluido   | Visible con banner azul     |
| `published` | Contenido aprobado      | Incluido   | Visible sin banner          |

### Modos de Construcción

#### Modo Preview (desarrollo local)

```bash
./serve.sh
```

- Muestra **todo** el contenido (draft, review, published)
- Los borradores aparecen con banners visuales de advertencia
- Variable: `DRAFT_MODE=true`

#### Modo Producción (publicación)

```bash
./scripts/build-public.sh
```

- Solo incluye contenido con `status: published`
- Los archivos draft/review se excluyen completamente
- Variable: `DRAFT_MODE=false`

### Workflow de Publicación

```
1. Crear contenido     →  status: draft
2. Completar contenido →  status: review  (opcional)
3. Aprobar contenido   →  status: published
4. Deploy automático   →  GitHub Actions (solo published)
```

#### Añadir front matter a archivos existentes

Si tienes archivos sin front matter, usa el script de utilidad:

```bash
python scripts/add-frontmatter.py
```

Este script:
- Añade `status: draft` a archivos nuevos
- Respeta archivos que ya tienen status definido
- Actualiza la lista `PUBLISHED_FILES` en el script para marcar contenido como publicado

### Cómo publicar nuevo contenido

1. **Edita el archivo** y cambia el status en el front matter:
   ```yaml
   ---
   status: published
   ---
   ```

2. **Verifica** que el contenido se muestra correctamente:
   ```bash
   ./serve.sh
   ```

3. **Haz commit** y push a la rama `main`

4. **GitHub Actions** construirá y desplegará automáticamente solo el contenido publicado

### Desactivar el Entorno Virtual

Cuando termines de trabajar:

```bash
deactivate
```

## ✍️ Contribuir

### Estructura de Archivos Markdown

Cada archivo debe seguir esta estructura:

```markdown
# Título Principal

Introducción breve del contenido.

## Sección 1

Contenido...

## Sección 2

Contenido...

---

*Última actualización: YYYY-MM-DD*
```

### Convenciones

#### Idioma

- Todo el contenido debe estar en **español**
- Usa terminología archivística estándar
- Mantén un tono profesional pero accesible

#### Formato

- Títulos en Sentence case (primera letra mayúscula)
- Usa listas para enumeraciones
- Incluye ejemplos prácticos cuando sea posible
- Añade capturas de pantalla en `docs/assets/images/`

#### Elementos Especiales

**Notas informativas:**

```markdown
!!! note "Título opcional"
    Contenido de la nota
```

**Consejos:**

```markdown
!!! tip "Consejo"
    Recomendación útil
```

**Advertencias:**

```markdown
!!! warning "Advertencia"
    Información importante
```

**Peligro/Crítico:**

```markdown
!!! danger "Importante"
    Información crítica
```

**Ejemplos:**

```markdown
!!! example "Ejemplo"
    Caso práctico
```

**Preguntas frecuentes:**

```markdown
??? question "¿Pregunta?"
    Respuesta expandible
```

### Imágenes

1. Guarda las imágenes en `docs/assets/images/`
2. Usa nombres descriptivos: `busqueda-avanzada-filtros.png`
3. Optimiza el tamaño (máximo 1920px de ancho)
4. Formatos recomendados: PNG para interfaces, JPG para fotos

Incluir en documentación:

```markdown
![Descripción de la imagen](../assets/images/nombre-imagen.png)
```

### Diagramas

Usa Mermaid para diagramas:

```markdown
\`\`\`mermaid
graph LR
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
\`\`\`
```

### Workflow de Contribución

1. **Fork** el repositorio
2. **Crea una rama** para tu contribución:
   ```bash
   git checkout -b mejora/descripcion-breve
   ```
3. **Realiza tus cambios** y verifica localmente con `mkdocs serve`
4. **Commit** con mensaje descriptivo:
   ```bash
   git commit -m "docs(user-guide): añadir sección sobre búsqueda por fechas"
   ```
5. **Push** a tu fork:
   ```bash
   git push origin mejora/descripcion-breve
   ```
6. Crea un **Pull Request** describiendo los cambios

### Formato de Commits

Seguimos el estándar [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(<ámbito>): <descripción>

[cuerpo opcional]
```

**Tipos:**

- `docs`: Cambios en documentación
- `fix`: Corrección de errores en la documentación
- `feat`: Nueva sección o contenido
- `style`: Cambios de formato (sin modificar contenido)
- `refactor`: Reorganización de contenido

**Ejemplos:**

```
docs(user-guide): añadir guía de búsqueda avanzada
fix(getting-started): corregir enlaces rotos
feat(admin-guide): añadir sección de monitorización
```

## 🔧 Tecnologías

- **[MkDocs](https://www.mkdocs.org/)**: Generador de sitios estáticos
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**: Tema moderno y responsive
- **[GitHub Actions](https://github.com/features/actions)**: CI/CD para deploy automático
- **[GitHub Pages](https://pages.github.com/)**: Hosting de la documentación

## 📝 Licencia

Esta documentación está bajo licencia [Apache License 2.0](LICENSE).

## 📧 Contacto

- **Issues**: [GitHub Issues](https://github.com/tu-org/nubarchiva-docs/issues)
- **Soporte**: support@nubarchiva.org
- **Web**: [nubarchiva.org](https://nubarchiva.org)

---

**Desarrollado con ❤️ para la comunidad archivística**
