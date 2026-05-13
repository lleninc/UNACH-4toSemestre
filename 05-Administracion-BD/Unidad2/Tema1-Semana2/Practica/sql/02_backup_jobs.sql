USE msdb;
GO

DECLARE @db SYSNAME = N'SistemaVentas';
DECLARE @backupDir NVARCHAR(400) = N'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema1-Semana2\Practica\Backups\';

-- FULL backup job at 17:30 daily
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = N'SistemaVentas - FULL 1730')
    EXEC msdb.dbo.sp_delete_job @job_name = N'SistemaVentas - FULL 1730';
GO

USE msdb;
GO
EXEC msdb.dbo.sp_add_job
    @job_name = N'SistemaVentas - FULL 1750',
    @enabled = 1,
    @description = N'Backup full diario a las 17:50 para SistemaVentas';
GO
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'SistemaVentas - FULL 1750',
    @step_name = N'FullBackup',
    @subsystem = N'TSQL',
    @command = N'DECLARE @file NVARCHAR(500) = N''E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema1-Semana2\Practica\Backups\SistemaVentas_Full_'' + CONVERT(CHAR(8), GETDATE(), 112) + N''_'' + REPLACE(CONVERT(CHAR(5), GETDATE(), 108), '':'' , '''') + N''.bak''; BACKUP DATABASE SistemaVentas TO DISK = @file WITH INIT, COMPRESSION, STATS = 5;',
    @database_name = N'master';
GO
EXEC msdb.dbo.sp_add_schedule
    @schedule_name = N'SistemaVentas - FULL 1750 Schedule',
    @freq_type = 4,
    @freq_interval = 1,
    @active_start_time = 175000;
GO
EXEC msdb.dbo.sp_attach_schedule
    @job_name = N'SistemaVentas - FULL 1750',
    @schedule_name = N'SistemaVentas - FULL 1750 Schedule';
GO
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'SistemaVentas - FULL 1750';
GO

-- Differential backup job every 10 minutes
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = N'SistemaVentas - DIFF 10MIN')
    EXEC msdb.dbo.sp_delete_job @job_name = N'SistemaVentas - DIFF 10MIN';
GO
EXEC msdb.dbo.sp_add_job
    @job_name = N'SistemaVentas - DIFF 10MIN',
    @enabled = 1,
    @description = N'Backup diferencial cada 10 minutos para SistemaVentas';
GO
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'SistemaVentas - DIFF 10MIN',
    @step_name = N'DiffBackup',
    @subsystem = N'TSQL',
    @command = N'DECLARE @file NVARCHAR(500) = N''E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema1-Semana2\Practica\Backups\SistemaVentas_Diff_'' + CONVERT(CHAR(8), GETDATE(), 112) + N''_'' + REPLACE(CONVERT(CHAR(5), GETDATE(), 108), '':'' , '''') + N''.bak''; BACKUP DATABASE SistemaVentas TO DISK = @file WITH DIFFERENTIAL, INIT, COMPRESSION, STATS = 5;',
    @database_name = N'master';
GO
-- calendarizacion cada 10 minutos (4 = daily, 1 = every day, 4 = minutes, 10 = every 10 minutes)
EXEC msdb.dbo.sp_add_schedule
    @schedule_name = N'SistemaVentas - DIFF 10MIN Schedule',
    @freq_type = 4,
    @freq_interval = 1,
    @freq_subday_type = 4,
    @freq_subday_interval = 10,
    @active_start_time = 000000;
GO
EXEC msdb.dbo.sp_attach_schedule
    @job_name = N'SistemaVentas - DIFF 10MIN',
    @schedule_name = N'SistemaVentas - DIFF 10MIN Schedule';
GO
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'SistemaVentas - DIFF 10MIN';
GO

-- Transaction log backup job every 2 minutes
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = N'SistemaVentas - LOG 2MIN')
    EXEC msdb.dbo.sp_delete_job @job_name = N'SistemaVentas - LOG 2MIN';
GO
EXEC msdb.dbo.sp_add_job
    @job_name = N'SistemaVentas - LOG 2MIN',
    @enabled = 1,
    @description = N'Backup transaccional cada 2 minutos para SistemaVentas';
GO
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'SistemaVentas - LOG 2MIN',
    @step_name = N'LogBackup',
    @subsystem = N'TSQL',
    @command = N'ALTER DATABASE SistemaVentas SET RECOVERY FULL; DECLARE @file NVARCHAR(500) = N''E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema1-Semana2\Practica\Backups\SistemaVentas_Log_'' + CONVERT(CHAR(8), GETDATE(), 112) + N''_'' + REPLACE(CONVERT(CHAR(5), GETDATE(), 108), '':'' , '''') + N''.trn''; BACKUP LOG SistemaVentas TO DISK = @file WITH INIT, COMPRESSION, STATS = 5;',
    @database_name = N'master';
GO
-- calendarizacion cada 2 minutos (4 = daily, 1 = every day, 4 = minutes, 2 = every 2 minutes)
EXEC msdb.dbo.sp_add_schedule
    @schedule_name = N'SistemaVentas - LOG 2MIN Schedule',
    @freq_type = 4,
    @freq_interval = 1,
    @freq_subday_type = 4,
    @freq_subday_interval = 2, -- cada 2 minutos se ejecuta el backup de log
    @active_start_time = 000000;
GO
EXEC msdb.dbo.sp_attach_schedule
    @job_name = N'SistemaVentas - LOG 2MIN',
    @schedule_name = N'SistemaVentas - LOG 2MIN Schedule';
GO
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'SistemaVentas - LOG 2MIN';
GO
