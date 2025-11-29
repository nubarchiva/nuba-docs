# Guía de Instalación

Esta guía te ayudará a instalar nubarchiva en tu entorno. Existen diferentes opciones según tu experiencia técnica y requisitos.

!!! warning "Documentación en Desarrollo"
    Esta es una guía preliminar. La documentación técnica completa para desarrolladores estará disponible próximamente.

## 🚀 Inicio Rápido con Docker

La forma más rápida de probar nubarchiva es usando Docker.

### Prerrequisitos

- Docker 20.10 o superior
- Docker Compose 2.0 o superior
- 4GB RAM mínimo (8GB recomendado)
- 10GB espacio en disco

### Instalación

1. **Clona el repositorio**:

```bash
git clone https://github.com/nubarchiva/nubarchiva.git
cd nubarchiva
```

!!! note "Repositorio Próximamente Público"
    El repositorio estará disponible públicamente próximamente.

2. **Inicia los servicios**:

```bash
docker-compose up -d
```

Este comando iniciará:
- Aplicación nubarchiva
- PostgreSQL (base de datos)
- Apache Solr (motor de búsqueda)

3. **Verifica la instalación**:

```bash
docker-compose ps
```

Deberías ver todos los servicios en estado "Up".

4. **Accede a la aplicación**:

Abre tu navegador en: [http://localhost:8080](http://localhost:8080)

**Credenciales por defecto**:
- Usuario: `admin`
- Contraseña: `admin`

!!! danger "Cambiar Credenciales"
    **IMPORTANTE**: Cambia las credenciales por defecto inmediatamente en un entorno de producción.

### Detener los Servicios

```bash
docker-compose down
```

Para eliminar también los datos:

```bash
docker-compose down -v
```

## 🖥️ Instalación Manual

Para entornos de producción o desarrollo avanzado.

### Requisitos del Sistema

#### Hardware Mínimo

| Componente | Mínimo     | Recomendado |
|------------|------------|-------------|
| CPU        | 2 cores    | 4+ cores    |
| RAM        | 4 GB       | 8 GB        |
| Disco      | 20 GB      | 100+ GB     |

#### Software

- **Java**: OpenJDK 8 o 11
- **Servidor de aplicaciones**: Tomcat 8.5+ o similar
- **Base de datos**: PostgreSQL 12+
- **Motor de búsqueda**: Apache Solr 3.5+ (versión específica en docs técnica)
- **Maven**: 3.6+ (para compilar desde fuentes)

### Pasos de Instalación

#### 1. Preparar Base de Datos

```sql
-- Crear base de datos
CREATE DATABASE nubarchiva
    WITH ENCODING='UTF8'
    LC_COLLATE='es_ES.UTF-8'
    LC_CTYPE='es_ES.UTF-8';

-- Crear usuario
CREATE USER nubarchiva_user WITH PASSWORD 'tu_password_seguro';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE nubarchiva TO nubarchiva_user;
```

#### 2. Configurar Apache Solr

```bash
# Descargar Solr (versión específica en docs técnica)
wget https://archive.apache.org/dist/lucene/solr/[VERSION]/...

# Extraer y configurar
# (Pasos detallados en documentación técnica)
```

#### 3. Compilar la Aplicación

```bash
# Clonar repositorio
git clone https://github.com/nubarchiva/nubarchiva.git
cd nubarchiva

# Compilar con Maven
mvn clean install -DskipTests

# El WAR se generará en target/nubarchiva.war
```

#### 4. Configurar la Aplicación

Crear archivo de configuración `nubarchiva.properties`:

```properties
# Base de datos
db.url=jdbc:postgresql://localhost:5432/nubarchiva
db.username=nubarchiva_user
db.password=tu_password_seguro

# Solr
solr.url=http://localhost:8983/solr/nubarchiva

# Directorio de archivos
files.path=/var/nubarchiva/files

# Logs
logs.path=/var/log/nubarchiva
```

#### 5. Desplegar en Tomcat

```bash
# Copiar WAR
cp target/nubarchiva.war /opt/tomcat/webapps/

# Copiar configuración
cp nubarchiva.properties /etc/nubarchiva/

# Reiniciar Tomcat
systemctl restart tomcat
```

#### 6. Inicializar Base de Datos

```bash
# Ejecutar scripts de inicialización
# (Incluidos en el paquete)
psql -U nubarchiva_user -d nubarchiva -f sql/init.sql
```

## ⚙️ Configuración Post-Instalación

### Verificar Instalación

1. Accede a: `http://tu-servidor:8080/nubarchiva`
2. Inicia sesión con credenciales por defecto
3. Verifica en Panel de Administración > Estado del Sistema

### Tareas Inmediatas

!!! danger "Seguridad"
    Completa estos pasos ANTES de poner en producción:

- [ ] Cambiar contraseña de administrador
- [ ] Configurar certificado SSL/TLS
- [ ] Configurar copias de seguridad automáticas
- [ ] Revisar configuración de firewall
- [ ] Configurar logs y monitorización

### Configurar Multi-tenancy (Opcional)

Si vas a hospedar múltiples instituciones:

1. Acceder a Panel de Administración
2. Ir a Configuración > Multi-tenancy
3. Crear nuevo tenant
4. Configurar subdominios o rutas

Ver [Guía de Multi-tenancy](#) _(en desarrollo)_ para detalles completos.

## 📦 Instalación desde Paquetes

### Debian/Ubuntu

_(Próximamente disponible)_

```bash
# Añadir repositorio
echo "deb https://repo.nubarchiva.org/debian stable main" | \
    sudo tee /etc/apt/sources.list.d/nubarchiva.list

# Instalar
sudo apt update
sudo apt install nubarchiva
```

### Red Hat/CentOS

_(Próximamente disponible)_

```bash
# Añadir repositorio
sudo yum-config-manager --add-repo https://repo.nubarchiva.org/rpm/

# Instalar
sudo yum install nubarchiva
```

## 🔄 Actualizaciones

### Docker

```bash
# Detener servicios
docker-compose down

# Actualizar imágenes
docker-compose pull

# Reiniciar
docker-compose up -d
```

### Manual

1. Hacer backup de base de datos
2. Hacer backup de archivos y configuración
3. Descargar nueva versión
4. Compilar y desplegar
5. Ejecutar scripts de migración si es necesario
6. Verificar funcionamiento

!!! warning "Backup Obligatorio"
    **SIEMPRE** haz backup completo antes de actualizar.

## 🐛 Solución de Problemas

### La aplicación no inicia

**Verificar logs**:

```bash
# Docker
docker-compose logs -f nubarchiva

# Manual
tail -f /var/log/tomcat/catalina.out
tail -f /var/log/nubarchiva/application.log
```

**Causas comunes**:
- Base de datos no accesible
- Solr no iniciado
- Permisos de archivos incorrectos
- Puerto 8080 ya en uso

### Errores de base de datos

```bash
# Verificar conexión
psql -U nubarchiva_user -d nubarchiva -h localhost

# Verificar permisos
psql -U postgres -c "\du"
```

### Solr no responde

```bash
# Verificar estado
curl http://localhost:8983/solr/admin/ping

# Reiniciar Solr
systemctl restart solr
```

### Problemas de rendimiento

- Aumentar memoria JVM en Tomcat
- Optimizar índices de Solr
- Revisar queries de base de datos lentos
- Configurar caché

## 📚 Siguientes Pasos

Después de la instalación:

1. 📖 [Configuración inicial](admin-guide/configuration/index.md)
2. 👥 [Gestión de usuarios](admin-guide/users/index.md)
3. 💾 [Configurar copias de seguridad](admin-guide/backup/index.md)
4. 🎨 [Personalizar la interfaz](customization/index.md)

## 🆘 Obtener Ayuda

### Documentación

- 📖 [Guía de Administración](admin-guide/index.md)
- 🔧 [Documentación técnica](#) _(en desarrollo)_

### Comunidad

- 💬 [Foro de la comunidad](https://community.nubarchiva.org) _(próximamente)_
- 🐛 [Reportar problemas](https://github.com/nubarchiva/nubarchiva/issues) _(próximamente)_

### Soporte Empresarial

¿Necesitas ayuda profesional para la instalación?

📧 [hello@nubarchiva.org](mailto:hello@nubarchiva.org)

Ofrecemos:
- Instalación asistida
- Configuración optimizada
- Migración desde otros sistemas
- Formación para administradores

## 📝 Notas de Versión

Consulta las notas de versión para:
- Nuevas funcionalidades
- Correcciones de bugs
- Cambios de configuración
- Requisitos actualizados

🔗 [Releases en GitHub](https://github.com/nubarchiva/nubarchiva/releases) _(próximamente)_

---

*Última actualización: 2025-11-29*
