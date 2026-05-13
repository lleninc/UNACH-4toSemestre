# Plan de respaldo y carga

- Inserción ficticia: cada 3 minutos desde Flask.
- Backup FULL: 17:30 diario.
- Backup DIFFERENTIAL: cada 10 minutos.
- Backup LOG: cada 2 minutos.
- Visualización: Flask consulta `msdb..backupset` y muestra el historial.
