# Configuración Básica

Configuración esencial de nubarchiva tras la instalación.

## 📁 Archivo de Configuración

`/etc/nubarchiva/nubarchiva.properties`

## 🔧 Parámetros Principales

```properties
# Base de datos
db.url=jdbc:postgresql://localhost:5432/nubarchiva
db.username=nubarchiva_user
db.password=PASSWORD

# Solr
solr.url=http://localhost:8983/solr/nubarchiva

# Directorios
files.path=/var/nubarchiva/files
logs.path=/var/log/nubarchiva
```

Ver detalles completos en: **[Instalación Manual](../deployment/bare-metal.md#paso-8-configurar-nubarchiva)**

---

*Última actualización: 2025-11-29*
