CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1 ;
  RETURN (
      SELECT(SELECT DISTINCT salary from Employee ORDER BY SALARY DESC LIMIT 1 OFFSET N) AS 
      getNthHighestSalary
  );
END