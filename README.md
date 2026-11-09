# Documentación de nubarchiva

Guías de uso de nubarchiva, escritas por tareas. Se publican en <https://docs.nubarchiva.es>.

## Cuándo se publica una página

Una página describe la aplicación tal como es en una versión concreta, y aparece en el sitio solo cuando esa versión
existe.

| Rama | Contiene | Se publica |
|------|----------|------------|
| `develop` | Las páginas de los cambios ya integrados en el producto, aunque aún no estén en una versión | No |
| `main` | Las páginas de lo que ya contiene una versión etiquetada | Sí, en cada push |

1. La página nueva o modificada entra en `develop` junto con el cambio de la aplicación que describe.
2. Cuando existe la versión etiquetada que contiene ese cambio, la página pasa de `develop` a `main`.
3. Cada push a `main` construye el sitio y lo despliega en GitHub Pages.

Las dos ramas se construyen en modo estricto en cada push y en cada pull request: un enlace roto o una página que
falta en la navegación hacen fallar la construcción.

## Previsualizar

Requiere Python 3.11 o posterior.

```bash
./serve.sh
```

Crea un entorno virtual en `venv/`, instala `requirements.txt` y sirve el sitio en <http://127.0.0.1:8000>, en modo
estricto. Para comprobar la construcción completa, como en GitHub Actions:

```bash
source venv/bin/activate
mkdocs build --strict
```

## Estructura

```
nuba-docs/
├── docs/                      Páginas en Markdown
│   ├── index.md               Portada
│   ├── user-guide/            Guías de uso, una carpeta por área de la aplicación
│   ├── assets/                Logos y hoja de estilos
│   └── CNAME                  Dominio del sitio
├── mkdocs.yml                 Configuración del sitio y navegación
├── requirements.txt           Versiones exactas de las dependencias
├── serve.sh                   Previsualización local
└── .github/workflows/         Construcción y despliegue
```

Una página nueva se añade también a `nav` en `mkdocs.yml`.

## Dependencias

El sitio se construye con MkDocs y el tema Material, con los complementos `search` y `minify`. `requirements.txt`
fija la versión exacta de cada paquete. Para actualizarlas:

```bash
printf 'mkdocs\nmkdocs-material\nmkdocs-minify-plugin\npymdown-extensions\n' \
  | uv pip compile - --python-version 3.11 --no-header --no-annotate -o requirements.txt
```

## Licencia

[Apache License 2.0](LICENSE).
