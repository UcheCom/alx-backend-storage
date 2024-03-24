--Script creates stored procedureComputeAverageWeightedScoreForUsers 
--that computes and store the average weighted score for all students.
--Procedure does not take any input.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE user AS u,
  (SELECT u.id, SUM(score * weight) / SUM(weight) AS weight_avg
  FROM users AS u
  JOIN corrections AS c ON u.id = c.user_id
  JOIN projects AS p ON c.projects = p.id
  GROUP BY u.id)
 AS w_a
 SET u.average_score = w_a.weight_avg
 WHERE u.id = w_a.id;
 END; //
 DELIMITER ;
