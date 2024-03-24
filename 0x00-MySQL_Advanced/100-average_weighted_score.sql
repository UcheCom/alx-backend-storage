-- Script creates procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
-- the procedure takes 1 input.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SET weight_avg_score = (
	    SELECT SUM(score * weight) / SUM(weight)
	    FROM users AS u
	    JOIN corrections AS c
	    ON u.id = c.user_id
	    JOIN projects AS p
	    ON c.project_id = p.id
	    WHERE u.id = user_id
	);

	UPDATE users 
	SET average_score = weight_avg_score;
END;
//
DELIMITER ;
