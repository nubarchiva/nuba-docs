# Actualización de nubarchiva

Guía para actualizar nubarchiva entre versiones de forma segura y eficiente.

!!! danger "Backup Obligatorio"
    **SIEMPRE** realiza un backup completo antes de actualizar. Ver: [Backup y Rollback](backup-and-rollback.md)

## 🎯 Antes de Empezar

### 1. Verifica tu Versión Actual

```bash
# En la interfaz web: Administración > Acerca de
# O en logs al iniciar:
grep "nubarchiva version" /var/log/nubarchiva/application.log
```

### 2. Consulta la Matriz de Compatibilidad

Ver: **[Matriz de Compatibilidad](compatibility-matrix.md)** para verificar paths de actualización soportados.

### 3. Planifica el Upgrade

Ver: **[Planificación del Upgrade](planning.md)** para preparar la actualización.

## 📊 Tipos de Actualización

### Patch Releases (2.25.0 → 2.25.1)

**Cambios**: Correcciones de bugs, parches de seguridad

**Complejidad**: ⭐ Baja

**Downtime**: Mínimo (5-15 minutos)

**Rollback**: Fácil

👉 **[Guía de Patch Upgrades](upgrade-paths/patch-upgrades.md)**

---

### Minor Releases (2.24 → 2.25)

**Cambios**: Nuevas funcionalidades, mejoras, correcciones

**Complejidad**: ⭐⭐ Media

**Downtime**: Moderado (15-30 minutos)

**Rollback**: Moderado

**Ejemplo**: 👉 **[Upgrade 2.24 → 2.25](upgrade-paths/2.24-to-2.25.md)**

---

### Major Releases (2.x → 3.x)

**Cambios**: Cambios arquitecturales, breaking changes

**Complejidad**: ⭐⭐⭐ Alta

**Downtime**: Significativo (1-4 horas)

**Rollback**: Complejo

**Ejemplo**: 👉 **[Upgrade 2.x → 3.x](upgrade-paths/2.x-to-3.x.md)**

---

## 🔧 Métodos de Actualización

Elige según tu tipo de instalación:

### Docker

Actualización mediante imágenes de contenedor.

👉 **[Actualizar Docker](methods/docker.md)**

```bash
# Resumen rápido
docker-compose pull
docker-compose up -d
```

---

### Instalación Manual (Bare Metal)

Actualización de WAR en Tomcat.

👉 **[Actualizar Bare Metal](methods/bare-metal.md)**

```bash
# Resumen rápido
1. Backup completo
2. Detener Tomcat
3. Reemplazar WAR
4. Ejecutar scripts migración
5. Iniciar Tomcat
6. Verificar
```

---

### Kubernetes

Rolling updates sin downtime.

👉 **[Actualizar Kubernetes](methods/kubernetes.md)** _(en desarrollo)_

---

## 🗄️ Migraciones

Aspectos críticos que pueden requerir atención especial:

### Migraciones de Base de Datos

Cambios en esquema, índices, datos.

👉 **[Guía de Migraciones DB](migration-guides/database-migrations.md)**

### Cambios de Configuración

Nuevos parámetros, cambios en properties.

👉 **[Cambios de Configuración](migration-guides/configuration-changes.md)**

### Breaking Changes

Incompatibilidades con versiones anteriores.

👉 **[Breaking Changes por Versión](migration-guides/breaking-changes.md)**

---

## ✅ Post-Actualización

Después de actualizar:

1. **[Verificar el Upgrade](post-upgrade/verification.md)** - Tests funcionales
2. **[Optimizaciones](post-upgrade/optimization.md)** - Mejorar rendimiento
3. **Monitorizar logs** primeros días

---

## 🚨 Solución de Problemas

Ver: **[Troubleshooting de Upgrades](troubleshooting.md)**

Problemas comunes:
- Error en migración de BD
- Aplicación no inicia después de upgrade
- Pérdida de configuración personalizada
- Problemas de rendimiento post-upgrade

---

## 📋 Checklist General

Pre-upgrade:

- [ ] Leer release notes de la versión destino
- [ ] Verificar compatibilidad en matriz
- [ ] Planificar ventana de mantenimiento
- [ ] **Backup completo** (BD + archivos + config)
- [ ] Probar en entorno desarrollo/staging
- [ ] Notificar a usuarios
- [ ] Preparar plan de rollback

Durante upgrade:

- [ ] Poner aplicación en modo mantenimiento
- [ ] Detener aplicación
- [ ] Backup de última hora
- [ ] Actualizar aplicación
- [ ] Ejecutar scripts de migración
- [ ] Verificar logs
- [ ] Probar funcionalidades críticas

Post-upgrade:

- [ ] Verificación funcional completa
- [ ] Monitorizar rendimiento
- [ ] Revisar logs primeros días
- [ ] Notificar usuarios del upgrade exitoso
- [ ] Documentar incidencias/aprendizajes

---

## 📚 Recursos Adicionales

- **[Changelog](../../changelog/index.md)** - Historial de cambios por versión
- **[Roadmap](../../roadmap.md)** - Versiones futuras planificadas
- **[Migration Scripts](https://github.com/nubarchiva/nubarchiva/tree/main/sql/migrations)** _(próximamente)_
- **[GitHub Releases](https://github.com/nubarchiva/nubarchiva/releases)** _(próximamente)_

---

## 🆘 Obtener Ayuda

### Comunidad

- 💬 [Foro](https://community.nubarchiva.org) _(próximamente)_
- 🐛 [Reportar problemas](https://github.com/nubarchiva/nubarchiva/issues) _(próximamente)_

### Soporte Empresarial

¿Necesitas ayuda profesional para el upgrade?

📧 [hello@nubarchiva.org](mailto:hello@nubarchiva.org)

Ofrecemos:
- **Análisis pre-upgrade** - Evaluación de impacto
- **Upgrade asistido** - Ejecutado por expertos
- **Soporte 24/7** - Durante ventana de mantenimiento
- **Rollback garantizado** - Si algo falla

---

*Última actualización: 2025-11-29*
