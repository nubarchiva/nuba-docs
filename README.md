# Manual de Usuario nubarchiva

[![Deploy Documentation](https://github.com/nubarchiva/nuba-docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/nubarchiva/nuba-docs/actions/workflows/deploy.yml)

Documentación oficial para usuarios de **nubarchiva**, el sistema de gestión archivística.

## 📖 Ver la Documentación

La documentación está publicada en: **[https://docs.nubarchiva.es](https://docs.nubarchiva.es)**

## 🏗️ Estructura del Proyecto

```
nuba-docs/
├── docs/                      # Contenido de la documentación
│   ├── index.md               # Página de inicio
│   ├── installation/          # Guía de instalación
│   ├── getting-started/       # Primeros pasos
│   ├── user-guide/            # Guía de usuario
│   ├── admin-guide/           # Guía de administración
│   ├── customization/         # Personalización
│   ├── changelog/             # Historial de versiones
│   └── assets/                # Recursos (imágenes, videos)
├── hooks/                     # Hooks de MkDocs
│   └── draft_filter.py        # Filtro de contenido draft/published
├── scripts/                   # Scripts de utilidad
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
git clone https://github.com/nubarchiva/nuba-docs.git
cd nuba-docs
```

2. Crea un entorno virtual de Python:

```bash
python3 -m venv venv
```

3. Activa el entorno virtual:

```bash
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🔄 Flujo de Trabajo

Este proyecto usa dos ramas principales:

| Rama | Propósito | Despliegue |
|------|-----------|------------|
| `develop` | Trabajo diario, borradores | No |
| `main` | Contenido listo para publicar | Automático a docs.nubarchiva.es |

### 1. Desarrollo (rama develop)

```bash
git checkout develop
source venv/bin/activate
DRAFT_MODE=true mkdocs serve
```

- Ves **todo** el contenido (drafts + published)
- Los borradores aparecen con banners visuales de advertencia
- Editas contenido, haces commits frecuentes

### 2. Previsualizar producción

Antes de publicar, verifica cómo se verá en producción:

```bash
source venv/bin/activate
DRAFT_MODE=false mkdocs serve
```

- Ves **solo** páginas con `status: published`
- Los enlaces a páginas no publicadas aparecen como **"texto" *(próximamente)***

### 3. Publicar

Cuando el contenido esté listo:

```bash
# Asegúrate de que las páginas tienen status: published
# Luego merge a main y push
git checkout main
git merge develop
git push origin main
```

GitHub Actions despliega automáticamente a `docs.nubarchiva.es`.

### 4. Volver a develop

```bash
git checkout develop
```

## 📋 Sistema de Publicación (Draft/Published)

Cada archivo `.md` debe tener un front matter YAML con el campo `status`:

```yaml
---
status: draft      # Borrador - en desarrollo
---

# Mi página
```

### Estados disponibles

| Estado | Descripción | Producción | Preview |
|--------|-------------|------------|---------|
| `draft` | Contenido en desarrollo | Excluido | Visible con banner amarillo |
| `review` | Pendiente de revisión | Excluido | Visible con banner azul |
| `published` | Contenido aprobado | Incluido | Visible sin banner |

### Comportamiento automático

El hook `draft_filter.py` realiza automáticamente:

1. **Filtra archivos**: Solo páginas con `status: published` aparecen en producción
2. **Filtra navegación**: Secciones vacías se ocultan automáticamente
3. **Convierte enlaces**: Enlaces a páginas draft se muestran como **"texto" *(próximamente)***

### Cómo publicar contenido

1. **Edita el archivo** y cambia el status:
   ```yaml
   ---
   status: published
   ---
   ```

2. **Previsualiza** en modo producción:
   ```bash
   DRAFT_MODE=false mkdocs serve
   ```

3. **Merge a main** y push:
   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```

4. **GitHub Actions** despliega automáticamente

### Añadir front matter a archivos existentes

Si tienes archivos sin front matter:

```bash
python scripts/add-frontmatter.py
```

## ✍️ Contribuir

### Estructura de Archivos Markdown

```markdown
---
status: draft
---

# Título Principal

Introducción breve del contenido.

## Sección 1

Contenido...

---

*Última actualización: YYYY-MM-DD*
```

### Convenciones

#### Idioma

- Todo el contenido en **español**
- Terminología archivística estándar
- Tono profesional pero accesible

#### Formato

- Títulos en Sentence case (primera letra mayúscula)
- Usa listas para enumeraciones
- Incluye ejemplos prácticos
- Capturas de pantalla en `docs/assets/images/`

#### Elementos Especiales

```markdown
!!! note "Nota"
    Información adicional

!!! tip "Consejo"
    Recomendación útil

!!! warning "Advertencia"
    Información importante

!!! danger "Peligro"
    Información crítica

!!! example "Ejemplo"
    Caso práctico

??? question "¿Pregunta?"
    Respuesta expandible
```

### Imágenes

1. Guarda en `docs/assets/images/`
2. Nombres descriptivos: `busqueda-avanzada-filtros.png`
3. Máximo 1920px de ancho
4. PNG para interfaces, JPG para fotos

```markdown
![Descripción](../assets/images/nombre-imagen.png)
```

### Diagramas con Mermaid

```markdown
​```mermaid
graph LR
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
​```
```

### Formato de Commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(<ámbito>): <descripción>
```

**Tipos:**
- `docs`: Cambios en documentación
- `fix`: Corrección de errores
- `feat`: Nueva sección o contenido
- `style`: Cambios de formato
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

- **Issues**: [GitHub Issues](https://github.com/nubarchiva/nuba-docs/issues)
- **Soporte**: hello@nubarchiva.es
- **Web**: [nubarchiva.es](https://nubarchiva.es)

---

**Desarrollado con cariño para la comunidad archivística**
