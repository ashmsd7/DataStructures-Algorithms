# Write your MySQL query statement below
Select (
Select salary
FROM Employee
WHERE salary < (
    Select MAX(salary) FROM Employee
) ORDER by salary DESC LIMIT 1)
AS SecondHighestSalary;

