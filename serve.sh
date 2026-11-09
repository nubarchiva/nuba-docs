#!/bin/bash
# Previsualiza el sitio en http://127.0.0.1:8000 con las dependencias de requirements.txt.
set -e
cd "$(dirname "$0")"

if [ ! -d venv ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --quiet -r requirements.txt

mkdocs serve --strict
