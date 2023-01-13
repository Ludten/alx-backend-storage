-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE a, b, c FLOAT;
  DECLARE cur1 CURSOR FOR SELECT user_id, (SUM(score * weight) / SUM(weight)) as avg FROM corrections JOIN projects ON corrections.project_id = projects.id GROUP BY corrections.user_id;
  DECLARE cur2 CURSOR FOR SELECT id FROM users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur1;
  OPEN cur2;

  read_loop: LOOP
    FETCH cur1 INTO a, b;
    FETCH cur2 INTO c;
    IF done THEN
      LEAVE read_loop;
    END IF;
    IF a = c THEN
      UPDATE users SET average_score = b WHERE id = a;
    END IF;
  END LOOP;

  CLOSE cur1;
  CLOSE cur2;
END;//
DELIMITER ;
