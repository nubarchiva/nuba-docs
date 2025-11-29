---
status: draft
---

# Requisitos del Sistema

Requisitos detallados para instalar y ejecutar nubarchiva en diferentes entornos.

## 🖥️ Requisitos de Hardware

### Entorno de Desarrollo/Pruebas

| Componente        | Mínimo    | Recomendado |
|-------------------|-----------|-------------|
| CPU               | 2 cores   | 2 cores     |
| RAM               | 4 GB      | 6 GB        |
| Disco             | 10 GB     | 20 GB       |
| Ancho de banda    | 10 Mbps   | 50 Mbps     |

### Entorno de Producción (Pequeño)

Para hasta 10,000 documentos y 10 usuarios concurrentes:

| Componente        | Mínimo    | Recomendado |
|-------------------|-----------|-------------|
| CPU               | 4 cores   | 8 cores     |
| RAM               | 8 GB      | 16 GB       |
| Disco             | 50 GB SSD | 100 GB SSD  |
| Ancho de banda    | 50 Mbps   | 100 Mbps    |

### Entorno de Producción (Mediano)

Para hasta 100,000 documentos y 50 usuarios concurrentes:

| Componente        | Mínimo     | Recomendado  |
|-------------------|------------|--------------|
| CPU               | 8 cores    | 16 cores     |
| RAM               | 16 GB      | 32 GB        |
| Disco             | 200 GB SSD | 500 GB SSD   |
| Ancho de banda    | 100 Mbps   | 1 Gbps       |

### Entorno de Producción (Grande)

Para más de 100,000 documentos y más de 50 usuarios concurrentes:

| Componente        | Recomendado  |
|-------------------|--------------|
| CPU               | 32+ cores    |
| RAM               | 64+ GB       |
| Disco             | 1+ TB SSD    |
| Ancho de banda    | 1+ Gbps      |

!!! tip "Arquitectura Distribuida"
    Para instalaciones grandes, considera distribuir los componentes en servidores separados:
    - Servidor de aplicación
    - Servidor de base de datos
    - Servidor de búsqueda (Solr)
    - Almacenamiento de archivos (NFS/S3)

## ☕ Java Runtime

### Versiones Soportadas

| Versión Java | Estado           | Notas                              |
|--------------|------------------|------------------------------------|
| OpenJDK 8    | ✅ Soportado     | Versión por defecto, probada       |
| OpenJDK 11   | ✅ Soportado     | Recomendado para nuevas instalaciones |
| OpenJDK 17   | ✅ Soportado     | LTS, mejor rendimiento             |
| Oracle JDK   | ⚠️ Compatible   | No necesario, usar OpenJDK         |
| Java 7 o <   | ❌ No soportado | Versión obsoleta                   |

### Configuración JVM Recomendada

**Desarrollo**:
```bash
JAVA_OPTS="-Xms512m -Xmx2g -XX:+UseG1GC"
```

**Producción (Pequeño)**:
```bash
JAVA_OPTS="-Xms2g -Xmx4g -XX:+UseG1GC -XX:MaxGCPauseMillis=200"
```

**Producción (Mediano/Grande)**:
```bash
JAVA_OPTS="-Xms4g -Xmx8g -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+HeapDumpOnOutOfMemoryError"
```

## 🗄️ Base de Datos

### PostgreSQL (Recomendado)

| Versión    | Estado           | Notas                         |
|------------|------------------|-------------------------------|
| 16.x       | ✅ Recomendado   | Última versión estable        |
| 15.x       | ✅ Soportado     | Versión estable               |
| 14.x       | ✅ Soportado     | Versión estable               |
| 13.x       | ✅ Soportado     | Versión estable               |
| 12.x       | ✅ Mínimo        | Versión mínima soportada      |
| 11.x o <   | ❌ No soportado  | Versión obsoleta              |

**Extensiones requeridas**: Ninguna (nubarchiva usa funcionalidad estándar)

### MySQL/MariaDB

_(Soporte en desarrollo)_

### Oracle Database

_(Soporte futuro para entornos enterprise)_

## 🔍 Motor de Búsqueda

### Apache Solr

| Versión | Estado          | Notas                              |
|---------|------------------|------------------------------------|
| 3.5.x   | ✅ Soportado    | Versión validada                   |
| 4.x     | ⚠️ Experimental | En fase de testing                 |
| 8.x+    | 🔄 Futuro       | Migración planificada              |

!!! warning "Versión Específica"
    nubarchiva actualmente está optimizado para Solr 3.5.x. Consulta la documentación técnica para migración a versiones superiores.

### Elasticsearch

_(Soporte futuro)_

## 🌐 Servidor de Aplicaciones

### Apache Tomcat (Recomendado)

| Versión  | Estado          | Notas                        |
|----------|-----------------|------------------------------|
| 9.x      | ✅ Recomendado  | Mejor rendimiento            |
| 8.5.x    | ✅ Soportado    | Versión mínima soportada     |
| 8.0.x    | ⚠️ Deprecado   | Actualizar a 8.5+            |
| 7.x o <  | ❌ No soportado | Versión obsoleta             |

### Otros Servidores

- **Jetty**: Compatible (documentación en desarrollo)
- **WildFly/JBoss**: Compatible (documentación en desarrollo)
- **WebSphere**: No probado
- **WebLogic**: No probado

## 💻 Sistema Operativo

### Linux (Recomendado)

| Distribución       | Versión        | Estado          |
|--------------------|----------------|-----------------|
| Ubuntu LTS         | 20.04, 22.04   | ✅ Recomendado  |
| Debian             | 11, 12         | ✅ Recomendado  |
| Red Hat Enterprise | 8.x, 9.x       | ✅ Soportado    |
| CentOS / Rocky     | 8.x, 9.x       | ✅ Soportado    |
| Amazon Linux       | 2, 2023        | ✅ Soportado    |

### Windows

| Versión           | Estado          | Notas                    |
|-------------------|-----------------|--------------------------|
| Windows Server    | ⚠️ Compatible   | Solo para desarrollo     |
| Windows 10/11     | ⚠️ Compatible   | Solo para desarrollo     |

!!! warning "Windows en Producción"
    No recomendado para producción. Usa Linux o contenedores Docker.

### macOS

| Versión    | Estado          | Notas                    |
|------------|-----------------|--------------------------|
| macOS 12+  | ⚠️ Compatible   | Solo para desarrollo     |

## 🐳 Docker

Si usas Docker:

| Componente      | Versión Mínima |
|-----------------|----------------|
| Docker Engine   | 20.10+         |
| Docker Compose  | 2.0+           |

**Requisitos de host**:

- Linux (recomendado) o Docker Desktop (dev)
- 4 GB RAM mínimo para el daemon Docker
- 20 GB espacio en disco

## 🌐 Navegadores Web

Para usuarios finales (acceso web):

| Navegador        | Versión Mínima | Notas                    |
|------------------|----------------|--------------------------|
| Chrome           | 90+            | ✅ Recomendado           |
| Firefox          | 88+            | ✅ Recomendado           |
| Safari           | 14+            | ✅ Soportado             |
| Edge             | 90+            | ✅ Soportado             |
| Internet Explorer| -              | ❌ No soportado          |

## 🔧 Herramientas de Construcción

Solo si vas a compilar desde código fuente:

| Herramienta | Versión Mínima | Notas                         |
|-------------|----------------|-------------------------------|
| Maven       | 3.6+           | Requerido para compilar       |
| Git         | 2.0+           | Para clonar repositorio       |

## 📦 Almacenamiento

### Almacenamiento de Archivos

nubarchiva almacena archivos binarios (documentos digitalizados, imágenes, PDFs):

- **Local**: Sistema de archivos local (para instalaciones pequeñas)
- **NFS**: Network File System (para instalaciones medianas)
- **S3**: Amazon S3 o compatible _(futuro)_

**Estimación de espacio**:

- Linux (recomendado) o Docker Desktop (dev)
- Documentos pequeños (~1 MB promedio): 1 GB por 1,000 documentos
- Documentos medianos (~10 MB promedio): 10 GB por 1,000 documentos
- Documentos grandes (~100 MB promedio): 100 GB por 1,000 documentos

### Backup

Planifica almacenamiento adicional para backups:

- **Base de datos**: 1-5 GB típicamente
- **Archivos**: Igual al almacenamiento principal
- **Retención**: 3x el espacio total (recomendado: 30 días de backups)

## 🔒 Red y Seguridad

### Puertos

| Servicio          | Puerto  | Protocolo | Acceso         |
|-------------------|---------|-----------|----------------|
| Aplicación web    | 8080    | HTTP      | Público        |
| Aplicación web    | 8443    | HTTPS     | Público        |
| PostgreSQL        | 5432    | TCP       | Interno        |
| Solr              | 8983    | HTTP      | Interno        |

### Firewall

Configuración típica:

```bash
# Permitir HTTP/HTTPS
ufw allow 80/tcp
ufw allow 443/tcp

# Permitir SSH (admin)
ufw allow 22/tcp

# Bloquear acceso directo a DB y Solr desde internet
ufw deny 5432/tcp
ufw deny 8983/tcp
```

### SSL/TLS

**Producción**: SSL/TLS es **obligatorio**

- Certificado válido (Let's Encrypt gratuito)
- TLS 1.2 o superior
- Configurar en reverse proxy (nginx/Apache)

## ☁️ Requisitos Cloud

### AWS

- **EC2**: t3.medium mínimo (producción: t3.large o superior)
- **RDS**: PostgreSQL db.t3.medium mínimo
- **S3**: Para almacenamiento de archivos (opcional)
- **VPC**: Configuración de red privada

### Azure

- **VM**: Standard_D2s_v3 mínimo
- **Azure Database for PostgreSQL**: 2 vCores mínimo
- **Blob Storage**: Para archivos (opcional)

### Google Cloud

- **Compute Engine**: n2-standard-2 mínimo
- **Cloud SQL**: PostgreSQL db-n1-standard-2 mínimo
- **Cloud Storage**: Para archivos (opcional)

## 📊 Monitorización

Herramientas recomendadas:

- **Logs**: Centralizar con ELK Stack, Graylog o similar
- **Métricas**: Prometheus + Grafana
- **APM**: New Relic, Datadog o similar (opcional)
- **Uptime**: UptimeRobot, Pingdom o similar

## ✅ Checklist Pre-Instalación

Antes de instalar, verifica:

- [ ] Hardware cumple requisitos mínimos
- [ ] Sistema operativo Linux actualizado
- [ ] Java 8/11/17 instalado
- [ ] PostgreSQL 12+ instalado o disponible
- [ ] Apache Solr disponible
- [ ] Tomcat 8.5+ instalado o disponible
- [ ] Puertos necesarios disponibles
- [ ] Espacio en disco suficiente
- [ ] Plan de backups definido
- [ ] Certificado SSL (producción)
- [ ] Firewall configurado

---

**Siguiente paso**: [Elegir método de instalación](index.md)

---

*Última actualización: 2025-11-29*
