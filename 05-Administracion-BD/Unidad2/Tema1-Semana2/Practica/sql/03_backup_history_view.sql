USE SistemaVentas;
GO

IF OBJECT_ID('dbo.vw_backup_history', 'V') IS NOT NULL
    DROP VIEW dbo.vw_backup_history;
GO

CREATE VIEW dbo.vw_backup_history AS
SELECT TOP (200)
    bs.backup_finish_date,
    CASE bs.type
        WHEN 'D' THEN 'FULL'
        WHEN 'I' THEN 'DIFF'
        WHEN 'L' THEN 'LOG'
        ELSE bs.type
    END AS backup_type,
    bs.name AS backup_name,
    CAST(bs.backup_size / 1024.0 / 1024.0 AS DECIMAL(18,2)) AS backup_size_mb,
    bmf.physical_device_name,
    bs.first_lsn,
    bs.last_lsn
FROM msdb.dbo.backupset bs
LEFT JOIN msdb.dbo.backupmediafamily bmf ON bs.media_set_id = bmf.media_set_id
WHERE bs.database_name = 'SistemaVentas';
GO
