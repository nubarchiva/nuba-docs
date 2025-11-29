---
status: published
---

# Instalación con Docker

La forma más rápida y sencilla de instalar nubarchiva usando Docker y Docker Compose.

## 🎯 Ventajas de Docker

- ✅ Instalación en minutos
- ✅ Entorno aislado y reproducible
- ✅ Fácil actualización
- ✅ Ideal para desarrollo y pruebas
- ✅ Válido para producción (con configuración adecuada)

## 📋 Prerrequisitos

### Software Necesario

- **Docker Engine**: 20.10 o superior
- **Docker Compose**: 2.0 o superior
- **Git**: Para clonar el repositorio

### Verificar Instalación

```bash
docker --version
# Docker version 24.0.0 o superior

docker-compose --version
# Docker Compose version v2.20.0 o superior
```

### Hardware Mínimo

- **CPU**: 2 cores
- **RAM**: 4 GB (8 GB recomendado)
- **Disco**: 10 GB libres (20 GB recomendado)

## 🚀 Instalación Rápida

### 1. Clonar Repositorio

```bash
git clone https://github.com/nubarchiva/nubarchiva.git
cd nubarchiva
```

!!! note "Repositorio Próximamente Público"
    El repositorio estará disponible públicamente próximamente.

### 2. Configurar Variables de Entorno (Opcional)

Crea un archivo `.env`:

```bash
# .env
POSTGRES_PASSWORD=tu_password_seguro
NUBARCHIVA_PORT=8080
POSTGRES_PORT=5432
SOLR_PORT=8983
```

### 3. Iniciar Servicios

```bash
docker-compose up -d
```

Este comando:
- Descarga las imágenes necesarias
- Crea los contenedores
- Inicia todos los servicios en segundo plano

### 4. Verificar Estado

```bash
docker-compose ps
```

Deberías ver:
```
NAME                STATUS              PORTS
nubarchiva-app      Up                  0.0.0.0:8080->8080/tcp
nubarchiva-db       Up                  5432/tcp
nubarchiva-solr     Up                  8983/tcp
```

### 5. Acceder a la Aplicación

Abre tu navegador en: [http://localhost:8080/nubarchiva](http://localhost:8080/nubarchiva)

**Credenciales por defecto**:
- Usuario: `admin`
- Contraseña: `admin`

!!! danger "Cambiar Credenciales"
    **IMPORTANTE**: Cambia las credenciales por defecto inmediatamente.

## 📁 Estructura docker-compose.yml

Ejemplo de configuración:

```yaml
version: '3.8'

services:
  # Base de datos PostgreSQL
  db:
    image: postgres:15-alpine
    container_name: nubarchiva-db
    environment:
      POSTGRES_DB: nubarchiva
      POSTGRES_USER: nubarchiva
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - nubarchiva-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U nubarchiva"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Apache Solr
  solr:
    image: solr:3.5
    container_name: nubarchiva-solr
    volumes:
      - solr-data:/opt/solr/data
      - ./solr/conf:/opt/solr/conf
    networks:
      - nubarchiva-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8983/solr/admin/ping"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Aplicación nubarchiva
  app:
    image: nubarchiva/nubarchiva:latest
    container_name: nubarchiva-app
    depends_on:
      db:
        condition: service_healthy
      solr:
        condition: service_healthy
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_NAME: nubarchiva
      DB_USER: nubarchiva
      DB_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
      SOLR_URL: http://solr:8983/solr/nubarchiva
      JAVA_OPTS: -Xms512m -Xmx2g
    ports:
      - "${NUBARCHIVA_PORT:-8080}:8080"
    volumes:
      - app-files:/var/nubarchiva/files
      - app-logs:/var/log/nubarchiva
    networks:
      - nubarchiva-net
    restart: unless-stopped

volumes:
  postgres-data:
  solr-data:
  app-files:
  app-logs:

networks:
  nubarchiva-net:
    driver: bridge
```

## ⚙️ Configuración Avanzada

### Persistencia de Datos

Los datos se almacenan en volúmenes Docker:

```bash
# Ver volúmenes
docker volume ls | grep nubarchiva

# Backup de volumen
docker run --rm -v nubarchiva_postgres-data:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/postgres-backup.tar.gz -C /data .
```

### Variables de Entorno

Personaliza mediante archivo `.env`:

```bash
# Base de datos
POSTGRES_DB=nubarchiva
POSTGRES_USER=nubarchiva
POSTGRES_PASSWORD=password_muy_seguro

# Aplicación
NUBARCHIVA_PORT=8080
JAVA_OPTS=-Xms1g -Xmx4g

# Solr
SOLR_PORT=8983
SOLR_HEAP=1g
```

### Recursos Limitados

Limita recursos por contenedor:

```yaml
services:
  app:
    # ...
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

## 📊 Monitorización

### Ver Logs

```bash
# Todos los servicios
docker-compose logs -f

# Solo aplicación
docker-compose logs -f app

# Solo últimas 100 líneas
docker-compose logs --tail=100 app
```

### Estadísticas de Recursos

```bash
docker stats
```

### Acceso a Contenedores

```bash
# Shell en contenedor de aplicación
docker-compose exec app bash

# Shell en PostgreSQL
docker-compose exec db psql -U nubarchiva
```

## 🔄 Operaciones Comunes

### Reiniciar Servicios

```bash
# Todos los servicios
docker-compose restart

# Solo aplicación
docker-compose restart app
```

### Detener Servicios

```bash
# Detener sin eliminar contenedores
docker-compose stop

# Detener y eliminar contenedores (mantiene volúmenes)
docker-compose down

# Detener y eliminar todo (incluyendo volúmenes)
docker-compose down -v
```

### Actualizar Imágenes

```bash
# Descargar nuevas versiones
docker-compose pull

# Recrear contenedores con nuevas imágenes
docker-compose up -d --force-recreate
```

### Limpiar Recursos

```bash
# Eliminar contenedores parados
docker container prune

# Eliminar imágenes sin usar
docker image prune

# Eliminar volúmenes sin usar (¡cuidado!)
docker volume prune
```

## 🔒 Producción con Docker

### SSL/TLS con Nginx

Usa nginx como reverse proxy:

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    networks:
      - nubarchiva-net
```

Configuración nginx:

```nginx
server {
    listen 80;
    server_name docs.ejemplo.org;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name docs.ejemplo.org;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    location / {
        proxy_pass http://app:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Backups Automatizados

Script de backup:

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d-%H%M%S)

# Backup base de datos
docker-compose exec -T db pg_dump -U nubarchiva nubarchiva | \
  gzip > "$BACKUP_DIR/db-$DATE.sql.gz"

# Backup archivos
docker run --rm \
  -v nubarchiva_app-files:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf "/backup/files-$DATE.tar.gz" -C /data .

# Retener solo últimos 30 días
find "$BACKUP_DIR" -name "*.gz" -mtime +30 -delete
```

Automatizar con cron:

```cron
# Backup diario a las 2 AM
0 2 * * * /path/to/backup.sh
```

### Monitorización con Prometheus

```yaml
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    ports:
      - "9090:9090"
    networks:
      - nubarchiva-net

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    networks:
      - nubarchiva-net
```

## 🐛 Solución de Problemas

### Contenedor no inicia

```bash
# Ver logs detallados
docker-compose logs app

# Verificar health checks
docker inspect nubarchiva-app | grep -A 10 Health
```

### Base de datos no conecta

```bash
# Verificar que PostgreSQL esté listo
docker-compose exec db pg_isready -U nubarchiva

# Probar conexión manual
docker-compose exec db psql -U nubarchiva -d nubarchiva -c "SELECT 1"
```

### Solr no responde

```bash
# Verificar logs de Solr
docker-compose logs solr

# Probar endpoint
curl http://localhost:8983/solr/admin/ping
```

### Puerto ya en uso

```bash
# Cambiar puerto en .env
echo "NUBARCHIVA_PORT=8081" >> .env

# Reiniciar
docker-compose up -d
```

### Sin espacio en disco

```bash
# Ver uso de volúmenes
docker system df -v

# Limpiar imágenes antiguas
docker image prune -a

# Limpiar contenedores parados
docker container prune
```

## 📚 Siguientes Pasos

- **[Configuración básica](../configuration/basic.md)** - Configurar parámetros
- **[Usuarios y permisos](../../admin-guide/users/index.md)** - Gestión de acceso
- **[Backups](../../admin-guide/backup/index.md)** - Estrategia de respaldo

---

*Última actualización: 2025-11-29*
