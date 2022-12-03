import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Klopot76',
    database='pds'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE my_first_db')
mycursor.execute('USE my_first_db')
mycursor.execute('CREATE TABLE student (id INT, name VARCHAR(255))')
mycursor.execute('CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), '
                 'salary INT(6))')
mycursor.execute('ALTER TABLE student ADD PRIMARY KEY(id)')
mycursor.execute('INSERT INTO student (id, name) VALUES (01, "John")')
mycursor.execute('INSERT INTO employee (name, salary) VALUES ("John", 10000)')

mycursor.execute('SELECT * FROM student')
stud_result = mycursor.fetchall()

mycursor.execute('SELECT * FROM employee')
empl_result = mycursor.fetchall()

for row in stud_result:
    print(row)

for row in empl_result:
    print(row)

