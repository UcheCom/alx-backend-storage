--Script creates stored procedureComputeAverageWeightedScoreForUsers 
--that computes and store the average weighted score for all students.
--Procedure does not take any input.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS u
  INNER JOIN (
    SELECT user_id, SUM(c.score * p.weight) AS total_w_s, SUM(p.weight) AS total_w
    FROM projects AS p
    INNER JOIN corrections c ON c.project_id = p.id
    GROUP BY user_id
 ) AS s ON u.id = s.user_id
 SET u.average_score = s.total_w_s / s.total_w;
 END; //
 DELIMITER ;
