import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = db_connection.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS task1")
    print("База данных 'task1' успешно создана или уже существует.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании базы данных: {err}")
    
db_connection.database = "task1"

Students = """
CREATE TABLE IF NOT EXISTS Students (
    SudentID INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(100),         
    Surname VARCHAR(100),  
    Faculty VARCHAR(100),
    DateOfBirth DATETIME
)
"""
try:
    cursor.execute(Students)
    print("Таблица 'Users' успешно создана.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании таблицы: {err}")
    
Teachers = """
CREATE TABLE IF NOT EXISTS Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(100),         
    Surname VARCHAR(100),  
    Department VARCHAR(100),   
)
"""
try:
    cursor.execute(Teachers)
    print("Таблица 'Users' успешно создана.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании таблицы: {err}")
    
Courses = """
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,         
    Title VARCHAR(100),  
    Description VARCHAR(500),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
)
"""
try:
    cursor.execute(Courses)
    print("Таблица 'Users' успешно создана.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании таблицы: {err}")
    
Exams = """
CREATE TABLE IF NOT EXISTS Exams (
    ExamID INT AUTO_INCREMENT PRIMARY KEY, 
    ExamDate DATETIME,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    MaxScore INT
)
"""
try:
    cursor.execute(Exams)
    print("Таблица 'Users' успешно создана.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании таблицы: {err}")

Grades = """
CREATE TABLE IF NOT EXISTS Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY, 
    FOREIGN KEY (SudentID) REFERENCES Students(SudentID),
    FOREIGN KEY (ExamID) REFERENCES Exams(ExamID),
    Score INT
)
"""
try:
    cursor.execute(Grades)
    print("Таблица 'Users' успешно создана.")
except mysql.connector.Error as err:
    print(f"Ошибка при создании таблицы: {err}")
    
def AddToTable(table_name):
    if table_name == "Students":
        AddToStudents()
    if table_name == "Teachers":
        AddToTeachers()
    if table_name == "Courses":
        AddToCourses()
    if table_name == "Exams":
        AddToExams()
    if table_name == "Grades":
        AddToGrades()

def AddToStudents():
    insert = "INSERT INTO Students (Name, Surname, Faculty, DateOfBirth) VALUES (%s, %s, %s, %s)"
    to_insert = [(input("Введите имя студента: "), input("Введите фамилию студента: "), input("Введите факультет студента: "), input("Введите дату рождения студента: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Students'.")
    except mysql.connector.Error as err:
        print(f"Ошибка при вставке данных: {err}")
        
def AddToTeachers():
    insert = "INSERT INTO Teachers (Name, Surname, Department) VALUES (%s, %s, %s)"
    to_insert = [(input("Введите имя преподавателя: "), input("Введите фамилию преподавателя: "), input("Введите кафедру преподавателя: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Teachers'.")
    except mysql.connector.Error as err:
        print(f"Ошибка при вставке данных: {err}")

def AddToCourses():
    insert = "INSERT INTO Courses (Title, Description VALUES (%s, %s)"
    to_insert = [(input("Введите название курса: "), input("Введите описание курса: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Teachers'.")
    except mysql.connector.Error as err:
        print(f"Ошибка при вставке данных: {err}")
        
def AddToExams():
    insert = "INSERT INTO Exams (ExamDate, MaxScore) VALUES (%s, %s)"
    to_insert = [(input("Введите дату экзамена: "), input("Введите максимальный балл: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Teachers'.")
    except mysql.connector.Error as err:
        print(f"Ошибка при вставке данных: {err}")
        
def AddToGrades():
    insert = "INSERT INTO Grades (Score) VALUES (%s)"
    to_insert = [(input("Введите балл: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Teachers'.")
    except mysql.connector.Error as err:
        print(f"Ошибка при вставке данных: {err}")
