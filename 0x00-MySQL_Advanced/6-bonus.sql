-- create a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
	SET @user = user_id,
	@project = (SELECT id FROM projects WHERE project_name = name),
	@scr = score;
	IF @project IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET @project = LAST_INSERT_ID();
	END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (@user, @project, @scr);
END//
DELIMITER ;
