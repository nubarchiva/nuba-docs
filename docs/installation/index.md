---
status: published
---

# Instalación de nubarchiva

Bienvenido a la guía de instalación de nubarchiva. Esta sección te ayudará a instalar y configurar el sistema según tus necesidades.

!!! warning "Documentación en Desarrollo"
    Esta es una guía preliminar. La documentación técnica completa está en desarrollo continuo.

## 🎯 Elige tu Método de Instalación

### 🚀 Quickstart con Docker (Recomendado)

**Ideal para**: Pruebas, desarrollo, demos

La forma más rápida de tener nubarchiva funcionando:

```bash
git clone https://github.com/nubarchiva/nuba-oss.git
cd nubarchiva
docker-compose up -d
```

Accede a: [http://localhost:8080](http://localhost:8080)

👉 **[Guía completa Docker](deployment/docker.md)**

---

### 🖥️ Instalación Manual

**Ideal para**: Producción, personalización avanzada

Instalación paso a paso en servidor dedicado.

👉 **[Guía de instalación manual](deployment/bare-metal.md)**

---

### 📦 Desde Paquetes

**Ideal para**: Administradores de sistemas Linux

_(Próximamente disponible)_

- **[Debian/Ubuntu](packages/debian-ubuntu.md)** - Paquetes .deb
- **[Red Hat/CentOS](packages/redhat-centos.md)** - Paquetes .rpm

---

### ☁️ Cloud

**Ideal para**: Despliegue en nube

_(En desarrollo)_

- **[Kubernetes](deployment/kubernetes.md)** - Orquestación de contenedores
- **[Cloud Providers](deployment/cloud.md)** - AWS, Azure, GCP

---

## 📋 Requisitos del Sistema

Antes de instalar, verifica que cumples los requisitos:

### Hardware Mínimo

| Componente | Mínimo     | Recomendado |
|------------|------------|-------------|
| CPU        | 2 cores    | 4+ cores    |
| RAM        | 4 GB       | 8 GB        |
| Disco      | 20 GB      | 100+ GB     |

### Software

- **Java**: OpenJDK 8, 11 o 17
- **Base de datos**: PostgreSQL 12+ (recomendado)
- **Motor de búsqueda**: Apache Solr 3.5+
- **Servidor de aplicaciones**: Tomcat 8.5+ (recomendado)

👉 **[Requisitos completos](requirements.md)**

---

## 🔧 Componentes

nubarchiva está compuesto por varios componentes que necesitas instalar y configurar:

### Base de Datos

Almacenamiento persistente de metadatos y configuración.

- **[PostgreSQL](database/postgresql.md)** ⭐ Recomendado
- **[MySQL](database/mysql.md)** _(futuro)_
- **[Oracle](database/oracle.md)** _(futuro)_

### Servidor de Aplicaciones

Contenedor para ejecutar la aplicación web.

- **[Apache Tomcat](app-server/tomcat.md)** ⭐ Recomendado
- **[Jetty](app-server/jetty.md)** _(alternativa)_
- **[WildFly](app-server/wildfly.md)** _(futuro)_

### Motor de Búsqueda

Indexación y búsqueda de texto completo.

- **[Apache Solr](search/solr.md)** ⭐ Principal
- **[Elasticsearch](search/elasticsearch.md)** _(futuro)_

---

## ⚙️ Configuración

Después de la instalación básica:

- **[Configuración básica](configuration/basic.md)** - Parámetros esenciales
- **[Multi-tenancy](configuration/multi-tenancy.md)** - Múltiples instituciones
- **[SSL/TLS](configuration/ssl.md)** - Seguridad en producción
- **[Optimización](configuration/performance.md)** - Performance tuning

---

## 🔄 Actualizaciones

- **[Guía de actualización](upgrade.md)** - Migración entre versiones

---

## 🐛 Solución de Problemas

¿Problemas durante la instalación?

- **[Troubleshooting](troubleshooting.md)** - Errores comunes y soluciones

---

## 📚 Después de Instalar

Una vez instalado nubarchiva:

1. 📖 **[Configuración inicial](../admin-guide/configuration/index.md)** - Primeros pasos como admin
2. 👥 **[Gestión de usuarios](../admin-guide/users/index.md)** - Crear usuarios y roles
3. 💾 **[Copias de seguridad](../admin-guide/backup/index.md)** - Protege tus datos
4. 🎨 **[Personalización](../customization/index.md)** - Adapta la interfaz

---

## 🆘 Obtener Ayuda

### Comunidad

- 💬 [Foro de la comunidad](https://community.nubarchiva.es) _(próximamente)_
- 🐛 [Reportar problemas](https://github.com/nubarchiva/nuba-oss/issues) _(próximamente)_
- 📖 [Documentación completa](https://docs.nubarchiva.es)

### Soporte Empresarial

¿Necesitas ayuda profesional para la instalación?

📧 [hello@nubarchiva.es](mailto:hello@nubarchiva.es)

Ofrecemos:
- **Instalación asistida** - Te ayudamos paso a paso
- **Configuración optimizada** - Tuning para tu caso de uso
- **Migración de datos** - Desde otros sistemas
- **Formación** - Para tu equipo técnico

---

*Última actualización: 2025-11-29*
