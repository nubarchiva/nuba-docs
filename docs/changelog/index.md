---
status: published
---

# Changelog

Historial de cambios de nubarchiva siguiendo el formato [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

!!! info "Versionado Semántico"
    nubarchiva sigue [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

## 📚 Navegación

- **[Por Versión](#versiones)** - Changelog completo de cada release
- **[Por Categoría](categories/features.md)** - Solo nuevas funcionalidades
- **[Breaking Changes](categories/breaking-changes.md)** - Cambios incompatibles
- **[GitHub Releases](https://github.com/nubarchiva/nuba-oss/releases)** _(próximamente)_

---

## Versiones

### [v2.25.0] - 2025-11-15

**[Changelog completo →](versions/v2.25.md)**

#### Added
- ✨ Mejoras en rendimiento de búsqueda (reducción 30% tiempo respuesta)
- ✨ Nuevo visor de documentos con soporte para más formatos
- ✨ Gestión mejorada de colecciones personales
- ✨ Exportación masiva de metadatos en formato CSV

#### Changed
- 🔄 Actualización a Spring 5.3.33
- 🔄 Actualización a Hibernate 5.4.33
- 🔄 Mejoras en interfaz de búsqueda avanzada
- 🔄 Optimización de consultas en base de datos

#### Fixed
- 🐛 Corregido error al descargar archivos >100MB
- 🐛 Solucionado problema de memoria en indexación masiva
- 🐛 Arreglada visualización de caracteres especiales en resultados
- 🐛 Corregido timeout en búsquedas complejas

#### Security
- 🔒 Actualización de dependencias con vulnerabilidades CVE-2024-xxxxx
- 🔒 Mejoras en validación de uploads

---

### [v2.24.0] - 2025-05-20

**[Changelog completo →](versions/v2.24.md)**

#### Added
- ✨ Soporte para Java 17
- ✨ API REST básica para consulta de documentos
- ✨ Integración con sistemas externos via webhooks
- ✨ Dashboard de administración mejorado

#### Changed
- 🔄 Migración a PostgreSQL 15
- 🔄 Actualización de interfaz de administración
- 🔄 Mejoras en logging y trazabilidad

#### Deprecated
- ⚠️ Soporte para Java 8 será eliminado en v2.26

#### Fixed
- 🐛 Corregidos múltiples bugs en gestión de usuarios
- 🐛 Solucionados problemas de caché en clustering
- 🐛 Arreglada exportación de metadatos en XML

---

### [v2.23.2] - 2025-03-10 (Patch)

#### Fixed
- 🐛 Hotfix: Corregida vulnerabilidad crítica de seguridad
- 🐛 Solucionado error al iniciar con PostgreSQL 16

---

### [v2.23.1] - 2025-02-05 (Patch)

#### Fixed
- 🐛 Corregido error de encoding en exportaciones
- 🐛 Solucionado problema de sesiones en cluster

---

### [v2.23.0] - 2024-12-01

**[Changelog completo →](versions/v2.23.md)**

#### Added
- ✨ Multi-institución mejorado
- ✨ Permisos granulares por documento
- ✨ Auditoría de accesos

#### Changed
- 🔄 Refactorización de módulo de búsqueda
- 🔄 Mejoras de rendimiento en carga de resultados

#### Fixed
- 🐛 Múltiples correcciones menores

---

### [v2.22.0] - 2024-06-15

**[Changelog completo →](versions/v2.22.md)**

#### Added
- ✨ Soporte para PostgreSQL 14
- ✨ Mejoras en búsqueda por facetas

---

## 🏷️ Categorías de Cambios

### Added
Nuevas funcionalidades añadidas.

**[Ver todas las funcionalidades →](categories/features.md)**

### Changed
Cambios en funcionalidades existentes.

### Deprecated
Funcionalidades que serán eliminadas en futuras versiones.

**[Ver deprecaciones →](categories/deprecations.md)**

### Removed
Funcionalidades eliminadas.

### Fixed
Correcciones de bugs.

**[Ver todas las correcciones →](categories/fixes.md)**

### Security
Cambios relacionados con seguridad.

---

## ⚠️ Breaking Changes

Cambios que rompen compatibilidad con versiones anteriores.

**[Ver todos los breaking changes →](categories/breaking-changes.md)**

**Resumen por versión**:

- **v2.24.0**: Cambio en formato de API REST (campo `createdDate` → `created_at`)
- **v2.23.0**: Eliminado soporte para Tomcat 7.x
- **v2.22.0**: Cambio en estructura de configuración multi-institución

---

## 📋 Formato de Versiones

### Major Release (x.0.0)
- Cambios arquitecturales significativos
- Breaking changes importantes
- Nuevas funcionalidades mayores
- Ejemplo: v2.0.0 → v3.0.0

### Minor Release (2.x.0)
- Nuevas funcionalidades
- Mejoras significativas
- Deprecaciones
- Sin breaking changes (o mínimos documentados)
- Ejemplo: v2.24.0 → v2.25.0

### Patch Release (2.25.x)
- Correcciones de bugs
- Parches de seguridad
- Mejoras menores
- Sin breaking changes
- Ejemplo: v2.25.0 → v2.25.1

---

## 🔗 Enlaces

- **[Roadmap](../roadmap.md)** - Versiones futuras planificadas
- **[Guía de Actualización](../installation/upgrade/index.md)** - Cómo actualizar
- **[Matriz de Compatibilidad](../installation/upgrade/compatibility-matrix.md)** - Versiones soportadas
- **[GitHub Releases](https://github.com/nubarchiva/nuba-oss/releases)** _(próximamente)_
- **[Migration Scripts](https://github.com/nubarchiva/nuba-oss/tree/main/sql/migrations)** _(próximamente)_

---

## 📅 Calendario de Releases

| Versión | Release     | Estado      | EOL         |
|---------|-------------|-------------|-------------|
| v3.0    | Q2 2027     | Desarrollo  | -           |
| v2.26   | Q1 2026     | Planificada | Q1 2028     |
| v2.25   | Nov 2025    | **Actual**  | Nov 2027    |
| v2.24   | May 2025    | Mantenimiento| May 2027   |
| v2.23   | Dic 2024    | Mantenimiento| Dic 2026   |
| v2.22   | Jun 2024    | EOL pronto  | Jun 2026    |

---

## 🔔 Suscribirse a Actualizaciones

Mantente informado de nuevos releases:

- 🐦 **Twitter/X**: @nubarchiva _(próximamente)_
- 📧 **Newsletter**: _(próximamente)_
- 📺 **GitHub Watch**: [nubarchiva/nubarchiva](https://github.com/nubarchiva/nuba-oss) _(próximamente)_
- 💬 **[Foro](https://community.nubarchiva.es)** _(próximamente)_

---

**Última actualización**: 2025-11-29

[v2.25.0]: versions/v2.25.md
[v2.24.0]: versions/v2.24.md
[v2.23.0]: versions/v2.23.md
[v2.22.0]: versions/v2.22.md
