SELECT COUNT(DISTINCT JOB_ID)  AS 'Кількість найменувань вакансій'
FROM employees;

SELECT COUNT(*) AS 'Number of emloyees in 90 dep.', ROUND(AVG(SALARY), 2) AS 'Average salary in 90 dep.'
FROM employees
WHERE DEPARTMENT_ID = 90;

SELECT JOB_ID AS 'Спеціальність', COUNT(EMPLOYEE_ID) AS 'Кількість працівників'
FROM employees
GROUP BY 1;

SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID
FROM employees;

SELECT FIRST_NAME, LAST_NAME, JOB_ID, DEPARTMENT_ID
FROM employees
JOIN departments USING (DEPARTMENT_ID)
JOIN locations USING (LOCATION_ID)
WHERE CITY = 'London';