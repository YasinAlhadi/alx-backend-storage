-- A stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score INT;
    DECLARE total_count INT;
    SELECT SUM(score) INTO total_score FROM corrections WHERE corrections.user_id = user_id;
    SELECT COUNT(*) INTO total_count FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = total_score / total_count WHERE users.id = user_id;
END$$
DELIMITER ;