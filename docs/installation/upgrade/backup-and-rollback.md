# Backup y Rollback

Procedimientos críticos de backup y recuperación para upgrades.

!!! danger "Obligatorio"
    **NUNCA** actualices sin backup completo y verificado.

## 💾 Componentes a Respaldar

1. **Base de datos PostgreSQL**
2. **Archivos digitales** (`/var/nubarchiva/files`)
3. **Configuración** (`/etc/nubarchiva`)
4. **Aplicación** (WAR actual)
5. **Índices Solr** (opcional)

## 🔄 Niveles de Rollback

### Nivel 1: Rollback Rápido
Sin cambios de esquema BD - 5-10 minutos

### Nivel 2: Con Restauración BD
Después de migración de esquema - 15-30 minutos

### Nivel 3: Rollback Completo
Incluye archivos y Solr - 30-60 minutos

## 📋 Procedimiento Detallado

_(Documentación completa en desarrollo)_

Scripts y procedimientos específicos estarán disponibles próximamente.

---

*Última actualización: 2025-11-29*
