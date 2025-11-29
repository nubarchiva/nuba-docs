#!/bin/bash
# Script para build de producción: solo contenido published
#
# Uso: ./scripts/build-public.sh
# Output: ./site/

set -e

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🏗️  Build de producción nubarchiva-docs${NC}"

# Cambiar al directorio del proyecto
cd "$(dirname "$0")/.."

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  No se encontró el entorno virtual. Creándolo...${NC}"
    python3 -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Verificar si están instaladas las dependencias
if ! python -c "import mkdocs" &> /dev/null; then
    echo -e "${YELLOW}⚠️  Instalando dependencias...${NC}"
    pip install -r requirements.txt
fi

# Modo producción: solo contenido published
export DRAFT_MODE=false

echo -e "${YELLOW}   DRAFT_MODE=false: Solo contenido con status=published${NC}"
echo ""

# Build de producción
# Nota: No usamos --strict porque hay enlaces a contenido draft que se resolverán
# cuando se publique más documentación
if mkdocs build; then
    echo ""
    echo -e "${GREEN}✅ Build completado exitosamente${NC}"
    echo -e "${GREEN}   Output: ./site/${NC}"
else
    echo ""
    echo -e "${RED}❌ Build fallido. Revisa los errores arriba.${NC}"
    exit 1
fi
