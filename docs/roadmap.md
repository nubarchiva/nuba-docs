---
status: draft
---

# Roadmap nubarchiva

Visión y planificación del desarrollo de nubarchiva.

!!! info "Roadmap Abierto"
    Este roadmap es orientativo y puede cambiar según feedback de la comunidad y necesidades del proyecto.

## 🎯 Visión

**nubarchiva** aspira a ser la plataforma open source de referencia para la gestión, preservación y difusión de archivos, combinando:

- **Estándares archivísticos** - Cumplimiento de normas internacionales
- **Tecnología moderna** - Stack actualizado y mantenible
- **Facilidad de uso** - Interfaz intuitiva para archiveros y usuarios finales
- **Escalabilidad** - Desde pequeños archivos hasta grandes instituciones
- **Comunidad activa** - Desarrollo colaborativo y transparente

## 📅 Versiones Planificadas

### v2.25 - Actual (Q4 2025)

**Estado**: ✅ Lanzada

**Enfoque**: Estabilidad y mejoras incrementales

**Principales funcionalidades**:
- Mejoras de rendimiento en búsqueda
- Optimización de interfaz de usuario
- Correcciones de bugs reportados en 2.24
- Mejoras en gestión de colecciones

**[Ver Changelog completo](changelog/versions/v2.25.md)**

---

### v2.26 (Q1 2026)

**Estado**: 🔄 En desarrollo

**Enfoque**: Modernización de búsqueda y API REST

**Funcionalidades planeadas**:

#### 🔍 Búsqueda Avanzada
- [ ] Migración a Apache Solr 8.x
- [ ] Búsqueda por facetas mejorada
- [ ] Autocompletado inteligente
- [ ] Búsqueda por similitud (más como este)

#### 🔌 API REST
- [ ] API REST completa para integración externa
- [ ] Documentación OpenAPI/Swagger
- [ ] Webhooks para eventos
- [ ] Rate limiting y autenticación OAuth2

#### 🎨 Interfaz
- [ ] Visor de documentos mejorado
- [ ] Previsualización de más formatos
- [ ] Modo oscuro en toda la aplicación

#### 🔧 Mejoras Técnicas
- [ ] Soporte completo para Java 17
- [ ] Actualización a Spring 6.x
- [ ] Mejoras en caché distribuida

---

### v2.27 (Q3 2026)

**Estado**: 📋 Planeada

**Enfoque**: Multi-idioma y accesibilidad

**Funcionalidades planeadas**:

#### 🌐 Internacionalización
- [ ] Interfaz multiidioma (ES, EN, FR, CA)
- [ ] Soporte para metadatos multiidioma
- [ ] Detección automática de idioma

#### ♿ Accesibilidad
- [ ] Cumplimiento WCAG 2.1 AA
- [ ] Navegación completa por teclado
- [ ] Lectores de pantalla optimizados
- [ ] Alto contraste y tamaños de fuente ajustables

#### 📱 Responsive
- [ ] Interfaz optimizada para tablets
- [ ] Vista móvil mejorada
- [ ] Progressive Web App (PWA)

---

### v3.0 (Q2 2027) - Major Release

**Estado**: 💭 Investigación

**Enfoque**: Modernización arquitectural

**Cambios principales**:

#### 🏗️ Arquitectura
- [ ] Migración a arquitectura de microservicios (opcional)
- [ ] Soporte nativo para contenedores y Kubernetes
- [ ] Event-driven architecture
- [ ] CQRS para operaciones complejas

#### ☁️ Cloud-Native
- [ ] Almacenamiento en S3/compatible
- [ ] Base de datos cloud-native (Aurora, Cloud SQL)
- [ ] Auto-scaling horizontal
- [ ] Multi-region support

#### 🔐 Seguridad
- [ ] SAML 2.0 / OAuth2 / OpenID Connect
- [ ] Autenticación multifactor (MFA)
- [ ] Auditoría completa de acciones
- [ ] Encriptación en reposo y tránsito

#### 🎨 Frontend Moderno
- [ ] Frontend SPA (React/Vue) opcional
- [ ] API GraphQL
- [ ] WebSockets para updates en tiempo real

#### 💾 Datos
- [ ] Soporte para MySQL/MariaDB
- [ ] Soporte para Elasticsearch (alternativa a Solr)
- [ ] Replicación y HA nativa

⚠️ **Breaking Changes**: Ver [Guía de Migración 2.x → 3.x](installation/upgrade/upgrade-paths/2.x-to-3.x.md)

---

## 🔬 Investigación y Desarrollo

Tecnologías y conceptos en evaluación:

### Inteligencia Artificial

- **OCR mejorado** - Reconocimiento automático de texto en imágenes
- **Clasificación automática** - ML para sugerir categorías y metadatos
- **Reconocimiento de entidades** - Extracción automática de nombres, lugares, fechas
- **Búsqueda semántica** - Búsqueda por significado, no solo keywords

### Blockchain

- **Certificación de autenticidad** - Timestamping en blockchain
- **Trazabilidad inmutable** - Historial inalterable de cambios
- **NFTs para digitalización** - Certificados digitales de documentos únicos

### Web3

- **Almacenamiento descentralizado** - IPFS/Arweave para preservación a largo plazo
- **Control descentralizado** - DAO para gobernanza comunitaria (exploratorio)

### Preservación Digital

- **PREMIS** - Soporte completo del estándar de metadatos de preservación
- **Validación de formatos** - Detección automática de formatos obsoletos
- **Migración automática** - Conversión proactiva a formatos vigentes

---

## 📊 Roadmap por Áreas

### Backend / Core

| Feature                        | v2.26 | v2.27 | v3.0 |
|--------------------------------|-------|-------|------|
| Solr 8.x                       | ✅    |       |      |
| Spring 6.x                     | ✅    |       |      |
| API REST completa              | ✅    |       |      |
| Java 21 support                |       | ✅    |      |
| Microservicios                 |       |       | ✅   |
| MySQL support                  |       |       | ✅   |
| Elasticsearch support          |       |       | ✅   |

### Frontend / UX

| Feature                        | v2.26 | v2.27 | v3.0 |
|--------------------------------|-------|-------|------|
| Visor mejorado                 | ✅    |       |      |
| Modo oscuro                    | ✅    |       |      |
| Multi-idioma                   |       | ✅    |      |
| WCAG 2.1 AA                    |       | ✅    |      |
| PWA                            |       | ✅    |      |
| SPA moderna (React/Vue)        |       |       | ✅   |

### Seguridad

| Feature                        | v2.26 | v2.27 | v3.0 |
|--------------------------------|-------|-------|------|
| OAuth2                         | ✅    |       |      |
| SAML 2.0                       |       |       | ✅   |
| MFA                            |       |       | ✅   |
| Auditoría completa             |       |       | ✅   |
| Encriptación en reposo         |       |       | ✅   |

### DevOps / Infraestructura

| Feature                        | v2.26 | v2.27 | v3.0 |
|--------------------------------|-------|-------|------|
| Docker optimizado              | ✅    |       |      |
| Helm Charts                    |       | ✅    |      |
| Auto-scaling                   |       |       | ✅   |
| Multi-region                   |       |       | ✅   |
| Observabilidad (OpenTelemetry) |       |       | ✅   |

---

## 🗳️ Influye en el Roadmap

### Community Wishlist

Las funcionalidades más solicitadas por la comunidad:

1. **API REST completa** (v2.26) - 🔥 Alta demanda
2. **Multi-idioma** (v2.27) - 🔥 Alta demanda
3. **PWA / Móvil** (v2.27) - ⭐ Demanda media
4. **OCR integrado** (Investigación) - ⭐ Demanda media
5. **SAML 2.0** (v3.0) - ⭐ Demanda media

### Cómo Proponer Features

Tienes tres formas de influir en el roadmap:

#### 1. GitHub Discussions

**Para**: Propuestas generales, discusión de ideas

[📝 Abrir discusión](https://github.com/nubarchiva/nuba-oss/discussions) _(próximamente)_

#### 2. Feature Requests

**Para**: Solicitudes específicas y detalladas

[💡 Crear feature request](https://github.com/nubarchiva/nuba-oss/issues/new?template=feature_request.md) _(próximamente)_

#### 3. Contribuir Código

**Para**: Implementar directamente la funcionalidad

Ver: [Guía de Contribución](community.md#contribuir-al-código)

---

## 🤝 Partners y Patrocinadores

### Partners Estratégicos

_(Próximamente - Programa en desarrollo)_

Organizaciones que apoyan activamente el desarrollo de nubarchiva:
- Acceso anticipado a nuevas features
- Influencia en el roadmap
- Soporte prioritario
- Reconocimiento público

### Patrocinio

¿Tu organización quiere acelerar el desarrollo de una feature específica?

📧 [hello@nubarchiva.es](mailto:hello@nubarchiva.es)

Opciones:
- **Feature Sponsorship** - Financia desarrollo de feature específica
- **Core Development** - Apoya desarrollo general
- **Infrastructure** - Dona recursos cloud/hardware

---

## 📈 Métricas de Desarrollo

### Velocidad de Release

- **Releases minor**: Cada 6 meses
- **Releases patch**: Según necesidad (1-2 al mes)
- **Releases major**: Cada 18-24 meses

### Soporte de Versiones

- **Versión actual**: Soporte completo (2 años)
- **Versión anterior**: Mantenimiento (1 año)
- **Versiones antiguas**: Solo seguridad crítica (6 meses)

Ver: [Matriz de Compatibilidad](installation/upgrade/compatibility-matrix.md)

---

## 🔔 Mantente Informado

- 📰 **[Changelog](changelog/index.md)** - Cambios en cada versión
- 🐦 **Twitter/X**: @nubarchiva _(próximamente)_
- 💬 **[Foro](https://community.nubarchiva.es)** _(próximamente)_
- 📧 **Newsletter**: _(próximamente)_

---

## 📝 Notas

- Este roadmap es orientativo y puede cambiar
- Las fechas son estimadas
- Las features pueden moverse entre versiones según prioridades
- La comunidad puede proponer y votar features

**Última actualización**: 2025-11-29

---

*¿Tienes una idea que no está en el roadmap? [Cuéntanosla](community.md) →*
