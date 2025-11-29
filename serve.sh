#!/bin/bash
# Script de ayuda para ejecutar el servidor de desarrollo de MkDocs

set -e

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Iniciando servidor de documentación nubarchiva${NC}"

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  No se encontró el entorno virtual. Creándolo...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Entorno virtual creado${NC}"
fi

# Activar entorno virtual
echo -e "${GREEN}📦 Activando entorno virtual...${NC}"
source venv/bin/activate

# Verificar si están instaladas las dependencias
if ! python -c "import mkdocs" &> /dev/null; then
    echo -e "${YELLOW}⚠️  Instalando dependencias...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependencias instaladas${NC}"
fi

# Modo preview: mostrar TODO el contenido (incluido drafts)
export DRAFT_MODE=true

# Iniciar servidor
echo -e "${GREEN}🌐 Iniciando servidor en http://127.0.0.1:8000${NC}"
echo -e "${YELLOW}   DRAFT_MODE=true: Mostrando todo el contenido (drafts con banners)${NC}"
echo -e "${YELLOW}   Presiona Ctrl+C para detener el servidor${NC}"
echo ""

mkdocs serve
