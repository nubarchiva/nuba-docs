---
status: draft
---

# Funcionalidades Deprecadas

Funcionalidades que serán eliminadas en futuras versiones.

!!! warning "Planifica la Migración"
    Estas funcionalidades aún funcionan pero dejarán de hacerlo próximamente.

## Actualmente Deprecado

### Java 8 (Desde v2.24)

**Será eliminado en**: v2.26 (Q1 2026)

**Recomendación**: Migrar a Java 11 o 17

**Razón**: Java 8 llegó a EOL, mejoras de rendimiento en versiones nuevas

---

### API Legacy de Búsqueda (Desde v2.24)

**Será eliminado en**: v3.0 (Q2 2027)

**Recomendación**: Migrar a nueva API REST

**Migración**:
```bash
# API Legacy (deprecada)
GET /search?q=term

# Nueva API REST
GET /api/v1/search?query=term
```

---

### Configuración XML para Solr (Desde v2.25)

**Será eliminado en**: v2.26 (Q1 2026)

**Recomendación**: Migrar a configuración JSON

---

_Última actualización: 2025-11-29_
