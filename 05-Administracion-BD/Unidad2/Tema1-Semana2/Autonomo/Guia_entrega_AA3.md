# Guia de entrega - AA3 U2T1 (ABD)

Este documento te ayuda a convertir el script en el informe PDF solicitado.

## Archivos creados

- `AA3_U2T1_RecuperacionFundamentos.sql`
- `AA3 CDIA-ABD U2T1.pdf` (consigna)

## 1) Creacion de base de datos de prueba

En el script se crea la base `RecuperacionFundamentos` y se incluyen mas tablas que el minimo solicitado:

- `Departamentos`
- `Empleados`
- `Cargos` (extra)
- `Proyectos` (extra)
- `EmpleadoProyecto` (extra)
- `HistorialSalario` (extra)
- `BitacoraCambios` (extra)

## 2) Estrategias de consistencia

Incluye restricciones:

- `PRIMARY KEY`
- `FOREIGN KEY`
- `CHECK`
- `UNIQUE`

Y pruebas de insercion invalida con `TRY...CATCH` para demostrar:

- Salario negativo (bloqueado por CHECK)
- Departamento inexistente (bloqueado por FK)

## 3) Control de concurrencia

El script incluye 3 casos (ejecutar en dos sesiones de SSMS):

- Lectura sucia (`READ UNCOMMITTED`)
- Lectura no repetible
- Lectura fantasma

Tambien incluye como resolver con:

- `READ COMMITTED`
- `REPEATABLE READ`
- `SERIALIZABLE`

## 4) Copias de seguridad

Incluye instrucciones para:

- Backup Full
- Backup Diferencial
- Backup Log (incremental transaccional)

Antes de ejecutar, crea y valida la carpeta:

- `E:\Backups\RecuperacionFundamentos\`

## 5) Planificacion de respaldos y recuperacion

Incluye en comentarios del script:

- Frecuencia de full/diff/log
- Almacenamiento local + externo
- RPO = 30 min
- RTO = 2 horas
- Prueba de restauracion mensual
- Automatizacion con SQL Server Agent

## Estructura sugerida para tu PDF

1. Portada (nombres, fecha, carrera, semestre)
2. Objetivo
3. Desarrollo por punto (1 al 5 de la consigna)
4. Capturas de evidencia:
   - Tablas creadas
   - Restricciones aplicadas
   - Errores controlados de consistencia
   - Ejecucion de casos de concurrencia
   - Resultado de backups
5. Conclusiones
6. Bibliografia (la de la guia docente y la unidad)

## Evidencias minimas que te conviene capturar

- `SELECT` de conteos finales de tablas
- Mensajes de error controlado en `TRY...CATCH`
- Resultado de consultas en concurrencia
- Mensaje de backup finalizado en FULL, DIFF y LOG
- Consulta de `msdb..backupset` (opcional) para ver historial de respaldos
