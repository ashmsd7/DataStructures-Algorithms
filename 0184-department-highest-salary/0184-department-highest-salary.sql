SELECT d.name as Department , e.name as Employee , e.salary as Salary from Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE e.salary = (
    SELECT Max(e2.salary) FROM Employee e2
    WHERE e2.departmentId = e.departmentId
)