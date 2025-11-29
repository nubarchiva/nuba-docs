# Breaking Changes

Cambios que rompen compatibilidad con versiones anteriores.

!!! danger "Atención"
    Estos cambios requieren acción manual durante el upgrade.

## v2.24.0

### API REST: Cambio en nombres de campos

**Campos renombrados**:
- `createdDate` → `created_at`
- `modifiedDate` → `updated_at`
- `documentId` → `id`

**Impacto**: Integraciones externas vía API

**Migración**:
```javascript
// Antes
const date = response.createdDate;

// Después
const date = response.created_at;
```

**[Ver changelog completo v2.24](../versions/v2.24.md)**

---

## v2.23.0

### Eliminado soporte Tomcat 7.x

**Impacto**: Instalaciones con Tomcat 7

**Migración**: Actualizar a Tomcat 8.5 o superior

**[Guía de migración →](../../installation/app-server/tomcat.md)**

---

_Más versiones próximamente_
