-- create a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	SET @user = user_id;
    UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = @user)
	WHERE user_id = id;
END//
DELIMITER ;

