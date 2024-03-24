--Script creates stored procedureComputeAverageWeightedScoreForUsers 
--that computes and store the average weighted score for all students.
--Procedure does not take any input.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users u
  INNER JOIN (
    SELECT user_id, SUM(c.score * p.weight) AS total_w_s, SUM(p.weight) AS total_w
    FROM projects p
    INNER JOIN corrections c ON c.project_id = p.id
    GROUP BY user_id
 ) AS scores ON u.id = scores.user_id
 SET u.average_score = scores.total_w_s / scores.total_w;
END; //
DELIMITER ;
