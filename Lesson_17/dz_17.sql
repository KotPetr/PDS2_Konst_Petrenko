SELECT COUNT(DISTINCT JOB_ID)  AS 'Кількість найменувань вакансій'
FROM employees;

SELECT COUNT(*) AS 'Number of emloyees in 90 dep.', ROUND(AVG(SALARY), 2) AS 'Average salary in 90 dep.'
FROM employees
WHERE DEPARTMENT_ID = 90; 

SELECT ROW_NUMBER() OVER(ORDER BY JOB_ID) AS 'Номер п/п', JOB_ID AS 'Фах', COUNT(EMPLOYEE_ID) AS 'Кількість працівників'
FROM employees
GROUP BY 2;

SELECT ROW_NUMBER() OVER(ORDER BY FIRST_NAME) AS ROW_NUM, FIRST_NAME, LAST_NAME, DEPARTMENT_ID
FROM employees;

SELECT FIRST_NAME, LAST_NAME, JOB_ID, DEPARTMENT_ID
FROM employees
JOIN departments USING (DEPARTMENT_ID)
JOIN locations USING (LOCATION_ID)
WHERE CITY = 'London';