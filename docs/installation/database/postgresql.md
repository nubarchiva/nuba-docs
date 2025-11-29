---
status: published
---

# PostgreSQL

Base de datos relacional recomendada para nubarchiva.

## ✅ Por qué PostgreSQL

- **Open source**: Licencia permisiva
- **Robusto**: Probado en producción
- **ACID**: Garantías transaccionales
- **Rendimiento**: Excelente para consultas complejas
- **Extensible**: Funciones y tipos personalizados
- **Comunidad**: Amplio soporte y documentación

## 📋 Versiones Soportadas

| Versión    | Estado           | Notas                         |
|------------|------------------|-------------------------------|
| 16.x       | ✅ Recomendado   | Última versión estable        |
| 15.x       | ✅ Soportado     | Versión estable               |
| 14.x       | ✅ Soportado     | Versión estable               |
| 13.x       | ✅ Soportado     | Versión estable               |
| 12.x       | ✅ Mínimo        | Versión mínima soportada      |
| 11.x o <   | ❌ No soportado  | Versión obsoleta              |

## 🔧 Instalación

### Ubuntu/Debian

```bash
# Instalar PostgreSQL 15
sudo apt update
sudo apt install -y postgresql-15 postgresql-contrib-15

# Verificar instalación
sudo systemctl status postgresql
```

### Red Hat/CentOS

```bash
# Instalar repositorio oficial
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Deshabilitar módulo PostgreSQL por defecto
sudo dnf -qy module disable postgresql

# Instalar PostgreSQL 15
sudo yum install -y postgresql15-server postgresql15-contrib

# Inicializar base de datos
sudo /usr/pgsql-15/bin/postgresql-15-setup initdb

# Habilitar e iniciar
sudo systemctl enable postgresql-15
sudo systemctl start postgresql-15
```

### Docker

```bash
docker run -d \
  --name nubarchiva-postgres \
  -e POSTGRES_DB=nubarchiva \
  -e POSTGRES_USER=nubarchiva \
  -e POSTGRES_PASSWORD=changeme \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15-alpine
```

## 🗃️ Configuración para nubarchiva

### Crear Base de Datos

```bash
sudo -u postgres psql
```

```sql
-- Crear base de datos con encoding UTF-8
CREATE DATABASE nubarchiva
    WITH
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_ES.UTF-8'
    LC_CTYPE = 'es_ES.UTF-8'
    TEMPLATE = template0
    CONNECTION LIMIT = -1;

-- Crear usuario
CREATE USER nubarchiva_user WITH PASSWORD 'password_muy_seguro';

-- Otorgar privilegios
GRANT ALL PRIVILEGES ON DATABASE nubarchiva TO nubarchiva_user;

-- Hacer propietario (opcional pero recomendado)
ALTER DATABASE nubarchiva OWNER TO nubarchiva_user;

-- Salir
\q
```

### Verificar Creación

```bash
psql -U nubarchiva_user -d nubarchiva -h localhost -W
```

```sql
-- Verificar versión
SELECT version();

-- Verificar encoding
SHOW SERVER_ENCODING;

-- Listar tablas (después de desplegar nubarchiva)
\dt

-- Salir
\q
```

## ⚙️ Configuración de PostgreSQL

### postgresql.conf

Ubicación típica: `/etc/postgresql/15/main/postgresql.conf`

**Para desarrollo**:

```ini
# Conexiones
max_connections = 100
shared_buffers = 128MB

# Memoria
effective_cache_size = 1GB
work_mem = 4MB
maintenance_work_mem = 64MB
```

**Para producción (servidor con 8GB RAM)**:

```ini
# Conexiones
max_connections = 200
shared_buffers = 2GB

# Memoria
effective_cache_size = 6GB
work_mem = 16MB
maintenance_work_mem = 512MB

# WAL
wal_buffers = 16MB
checkpoint_completion_target = 0.9

# Planner
random_page_cost = 1.1  # Para SSD, 4.0 para HDD
effective_io_concurrency = 200  # Para SSD

# Logs (producción)
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
log_rotation_age = 1d
log_rotation_size = 100MB
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '
log_min_duration_statement = 1000  # Log queries > 1s
```

Después de modificar:

```bash
sudo systemctl restart postgresql
```

### pg_hba.conf

Ubicación típica: `/etc/postgresql/15/main/pg_hba.conf`

**Desarrollo (permitir localhost)**:

```ini
# TYPE  DATABASE        USER              ADDRESS          METHOD
local   all             postgres                           peer
local   all             all                                peer
host    nubarchiva      nubarchiva_user   127.0.0.1/32     md5
host    nubarchiva      nubarchiva_user   ::1/128          md5
```

**Producción (red local)**:

```ini
# TYPE  DATABASE        USER              ADDRESS          METHOD
local   all             postgres                           peer
host    nubarchiva      nubarchiva_user   10.0.0.0/24      md5
host    nubarchiva      nubarchiva_user   127.0.0.1/32     md5
```

Después de modificar:

```bash
sudo systemctl reload postgresql
```

## 🔧 Optimización

### Análisis de Queries

```sql
-- Habilitar extensión pg_stat_statements
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Ver queries más lentas
SELECT
  calls,
  total_exec_time,
  mean_exec_time,
  query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

### Vacuum y Analyze

```sql
-- Vacuum manual (liberar espacio)
VACUUM VERBOSE ANALYZE;

-- Vacuum específico de tabla
VACUUM VERBOSE ANALYZE nombre_tabla;
```

Configurar autovacuum en `postgresql.conf`:

```ini
autovacuum = on
autovacuum_max_workers = 3
autovacuum_naptime = 1min
```

### Índices

```sql
-- Ver índices de una tabla
\d nombre_tabla

-- Ver índices sin usar (candidatos para eliminar)
SELECT
  schemaname,
  tablename,
  indexname,
  idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexname NOT LIKE 'pg_%';
```

## 💾 Backups

### Backup Manual

```bash
# Backup completo
pg_dump -U nubarchiva_user -h localhost nubarchiva > backup.sql

# Backup comprimido
pg_dump -U nubarchiva_user -h localhost nubarchiva | gzip > backup.sql.gz

# Backup formato custom (más rápido restauración)
pg_dump -U nubarchiva_user -h localhost -Fc nubarchiva > backup.dump
```

### Restauración

```bash
# Desde SQL
psql -U nubarchiva_user -d nubarchiva < backup.sql

# Desde SQL comprimido
gunzip -c backup.sql.gz | psql -U nubarchiva_user -d nubarchiva

# Desde formato custom
pg_restore -U nubarchiva_user -d nubarchiva backup.dump
```

### Backup Automatizado

Script `/usr/local/bin/backup-nubarchiva-db.sh`:

```bash
#!/bin/bash
set -e

BACKUP_DIR="/backups/postgresql"
DATE=$(date +%Y%m%d-%H%M%S)
RETENTION_DAYS=30

mkdir -p "$BACKUP_DIR"

# Backup
pg_dump -U nubarchiva_user -h localhost nubarchiva | \
  gzip > "$BACKUP_DIR/nubarchiva-$DATE.sql.gz"

# Limpiar backups antiguos
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete

echo "Backup completado: $DATE"
```

Cron job:

```bash
sudo crontab -e
# Añadir:
0 2 * * * /usr/local/bin/backup-nubarchiva-db.sh >> /var/log/backup-db.log 2>&1
```

## 📊 Monitorización

### Conexiones Activas

```sql
SELECT
  count(*) as total,
  state
FROM pg_stat_activity
WHERE datname = 'nubarchiva'
GROUP BY state;
```

### Tamaño de Base de Datos

```sql
-- Tamaño total
SELECT pg_size_pretty(pg_database_size('nubarchiva'));

-- Tamaño por tabla
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

### Actividad de Disco

```sql
SELECT
  datname,
  blks_read,
  blks_hit,
  round(blks_hit::numeric / (blks_read + blks_hit) * 100, 2) as cache_hit_ratio
FROM pg_stat_database
WHERE datname = 'nubarchiva';
```

### Herramientas Externas

- **pgAdmin**: GUI para administración
- **pgBadger**: Análisis de logs
- **pg_top**: Monitorización en tiempo real
- **Prometheus + postgres_exporter**: Métricas

## 🔒 Seguridad

### Usuario con Privilegios Mínimos

```sql
-- Crear usuario solo lectura
CREATE USER nubarchiva_readonly WITH PASSWORD 'password_readonly';
GRANT CONNECT ON DATABASE nubarchiva TO nubarchiva_readonly;
GRANT USAGE ON SCHEMA public TO nubarchiva_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO nubarchiva_readonly;
```

### SSL/TLS

En `postgresql.conf`:

```ini
ssl = on
ssl_cert_file = '/etc/ssl/certs/server.crt'
ssl_key_file = '/etc/ssl/private/server.key'
```

En `pg_hba.conf`:

```ini
hostssl  nubarchiva  nubarchiva_user  0.0.0.0/0  md5
```

### Cambiar Contraseña

```sql
ALTER USER nubarchiva_user WITH PASSWORD 'nueva_password_segura';
```

## 🐛 Solución de Problemas

### No se puede conectar

```bash
# Verificar que PostgreSQL está corriendo
sudo systemctl status postgresql

# Verificar puerto
sudo netstat -tlnp | grep 5432

# Probar conexión local
psql -U postgres -c "SELECT 1"
```

### Queries Lentas

```sql
-- Ver queries en ejecución
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE state = 'active'
  AND query NOT LIKE '%pg_stat_activity%'
ORDER BY duration DESC;

-- Matar query específica
SELECT pg_terminate_backend(pid);
```

### Espacio en Disco

```bash
# Ver espacio usado por PostgreSQL
sudo du -sh /var/lib/postgresql/15/main

# Vacuum full (requiere downtime)
sudo -u postgres psql nubarchiva -c "VACUUM FULL"
```

## 📚 Recursos

- **Documentación oficial**: https://www.postgresql.org/docs/
- **Wiki PostgreSQL**: https://wiki.postgresql.org/
- **PgTune**: https://pgtune.leopard.in.ua/ (configuración recomendada)

---

*Última actualización: 2025-11-29*
