# Practica - SistemaVentas

Sistema pequeño en Flask para poblar la base `SistemaVentas`, consultar su estado y visualizar el historial de respaldos.

## Componentes

- `app.py`: interfaz web con estadísticas y tabla de respaldos.
- `database.py`: conexión a SQL Server, creación de tablas faltantes y generación de ventas ficticias.
- `sql/01_schema.sql`: script de esquema y datos base.
- `sql/02_backup_jobs.sql`: crea jobs de SQL Agent para backup full, diferencial y log.
- `sql/03_backup_history_view.sql`: vista para consultar historial de respaldos.

## Requisitos

- Python 3.11+.
- SQL Server con la base `SistemaVentas`.
- SQL Server Agent habilitado para ejecutar los jobs automáticos.

## Instalación

```bash
pip install -r requirements.txt
```

## Configuración

Variables opcionales:

- `SQL_SERVER` (por defecto `FRANCIS`)
- `SQL_DATABASE` (por defecto `SistemaVentas`)
- `SQL_DRIVER` (por defecto `ODBC Driver 17 for SQL Server`)
- `SQL_TRUSTED_CONNECTION` (`yes` por defecto)
- `SQL_USERNAME` y `SQL_PASSWORD` si usas autenticación SQL
- `SQL_BACKUP_DIR` para cambiar la carpeta de backups
- `DISABLE_SCHEDULER=1` si no quieres que Flask inserte ventas cada 3 minutos

## Flujo de uso

1. Ejecuta `sql/01_schema.sql` en SQL Server.
2. Ejecuta `sql/02_backup_jobs.sql` para crear los jobs de respaldo.
3. Ejecuta `sql/03_backup_history_view.sql` si quieres consultar respaldos como vista.
4. Inicia la app:

```bash
python app.py
```

5. Abre `http://127.0.0.1:5000`.

## Qué hace la app

- Inserta una venta ficticia automáticamente cada 3 minutos.
- Muestra contadores de productos, clientes, ventas e ingresos.
- Lista el historial de backups detectado en `msdb`.
- Permite insertar una venta manual desde el botón de la pantalla.

## Respaldo solicitado

- Full: 17:30 diario.
- Diferencial: cada 10 minutos.
- Log: cada 2 minutos.

Los scripts de `sql/02_backup_jobs.sql` dejan ese comportamiento listo para SQL Server Agent.
