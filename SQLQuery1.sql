-- Create the studyHours database
CREATE DATABASE studyHours;

-- Switch to the studyHours database
USE studyHours;


-- Create the student table
CREATE TABLE student (
    session_id INT PRIMARY KEY IDENTITY,
    subject_name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    hours_studied INT NOT NULL,
);


CREATE PROCEDURE displayTotalHours
AS
BEGIN
	SELECT SUM(hours_studied) AS total_hours
	FROM student;
END;


CREATE FUNCTION dbo.GetTotalStudyHoursForSubject
(
    @SubjectName NVARCHAR(255)
)
RETURNS INT
AS
BEGIN
    DECLARE @TotalHours INT;

    SELECT @TotalHours = SUM(hours_studied)
    FROM student
    WHERE subject_name = @SubjectName;

    RETURN @TotalHours;
END;


CREATE TRIGGER trg_read_only
ON student
INSTEAD OF INSERT
AS 
BEGIN
	PRINT('INSERT operations are not allowed on this table for now.')
END;

ENABLE TRIGGER trg_read_only ON student;
DISABLE TRIGGER trg_read_only ON student;


SELECT dbo.GetTotalStudyHoursForSubject('algo') AS TotalStudyHours;
SELECT * FROM student;