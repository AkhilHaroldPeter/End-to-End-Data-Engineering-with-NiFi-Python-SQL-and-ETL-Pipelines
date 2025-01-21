use DEProject1



IF OBJECT_ID('batch_metadata', 'U') IS NULL 
BEGIN
    CREATE TABLE batch_metadata (
        batch_id INT IDENTITY(1,1) PRIMARY KEY, --ingestion
        filename VARCHAR(255),--ingestion
        source_system VARCHAR(50),--ingestion
        file_size_bytes VARCHAR(10),--ingestion
        num_records INT,
		file_modified DATETIME,  -- Store the file's last modified timestamp
        ingestion_status VARCHAR(20) CHECK (ingestion_status IN ('SUCCESS', 'FAILED', 'IN_PROGRESS')),--ingestion
        ingestion_start_time DATETIME,--ingestion
        ingestion_end_time DATETIME,--ingestion
        processing_status VARCHAR(20) CHECK (processing_status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED')),
        processing_start_time DATETIME,
        processing_end_time DATETIME,
        loading_status VARCHAR(20) CHECK (loading_status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED')),
        loading_start_time DATETIME,
        loading_end_time DATETIME,
        error_message TEXT NULL,
        retry_attempts INT DEFAULT 0,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE()
    );
END;

INSERT INTO batch_metadata (
    filename, 
    source_system, 
    file_size, 
    file_modified, 
    ingestion_status, 
    ingestion_start_time, 
    ingestion_end_time, 
    processing_status, 
    processing_start_time, 
    processing_end_time, 
    loading_status, 
    loading_start_time, 
    loading_end_time, 
    error_message, 
    retry_attempts
) 



INSERT INTO batch_metadata (filename, file_path, file_size, num_records, ingestion_status, ingestion_start_time)
VALUES (?, ?, ?, ?, 'IN_PROGRESS', GETDATE());





	IF OBJECT_ID('trg_update_timestamp', 'TR') IS NOT NULL
		DROP TRIGGER trg_update_timestamp;
	GO

	CREATE TRIGGER trg_update_timestamp
	ON batch_metadata
	AFTER UPDATE
	AS
	BEGIN
		SET NOCOUNT ON;

		UPDATE batch_metadata
		SET updated_at = GETDATE()
		WHERE batch_id IN (SELECT DISTINCT batch_id FROM inserted);
	END;
	GO


SELECT SCOPE_IDENTITY() AS batch_id;