-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	SET @user = user_id;
    UPDATE users SET average_score = (
		SELECT (SUM(score * weight) / SUM(weight)) as avg
		FROM corrections JOIN projects
		ON corrections.project_id = projects.id
		WHERE corrections.user_id = @user
	)
	WHERE user_id = id;
END//
DELIMITER ;
