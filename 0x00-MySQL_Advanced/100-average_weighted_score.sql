-- Script creates procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
-- the procedure takes 1 input.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	UPDATE users 
	SET average_score = 
	(SELECT SUM(p.weight * c.score) / SUM(p.weight) FROM projects p, corrections c WHERE c.user_id=user_id AND p.id=project_id)
	WHERE users.id=user_id;
END;
//
DELIMITER ;
