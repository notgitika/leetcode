'''
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the name of 
the employee whose ID is employee_id.


Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the salary of 
the employee whose ID is employee_id.


Write an SQL query to report the IDs of all the 
employees with missing information. The information of an employee is missing if:

    The employee\'s name is missing, or
    The employee\'s salary is missing.

Return the result table ordered by employee_id in ascending order.
'''

SELECT Employees.employee_id from 

Employees LEFT JOIN Salaries on Employees.employee_id = Salaries.employee_id

where Salaries.salary IS NULL 

UNION

SELECT Salaries.employee_id from 

Employees RIGHT JOIN Salaries on Employees.employee_id = Salaries.employee_id

where Employees.name IS NULL 

ORDER BY employee_id ASC