-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
	DECLARE d INT;

	IF b = 0 THEN
		SET d = 0;
		RETURN d;
	END IF;

	RETURN (a / b);
END
//
DELIMITER ;