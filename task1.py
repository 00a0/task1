import sqlite3
import random

db_connection = sqlite3.connect('task1.db')
cursor = db_connection.cursor()

# №1

def create_tables():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name TEXT NOT NULL,         
            Surname TEXT NOT NULL,  
            Department TEXT NOT NULL,
            DateOfBirth DATE NOT NULL
        )
        """)
        print("Таблица 'Students' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Students': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            TeacherID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name TEXT NOT NULL,         
            Surname TEXT NOT NULL,  
            Department TEXT NOT NULL
        )
        """)
        print("Таблица 'Teachers' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Teachers': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY AUTOINCREMENT,         
            Title TEXT NOT NULL,  
            Description TEXT,
            TeacherID INTEGER,
            FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
        )
        """)
        print("Таблица 'Courses' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Courses': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Exams (
            ExamID INTEGER PRIMARY KEY AUTOINCREMENT, 
            ExamDate DATE NOT NULL,
            MaxScore INTEGER NOT NULL,
            CourseID INTEGER,
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        )
        """)
        print("Таблица 'Exams' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Exams': {err}")
    
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Grades (
            GradeID INTEGER PRIMARY KEY AUTOINCREMENT, 
            StudentID INTEGER,
            ExamID INTEGER,
            Score INTEGER NOT NULL,
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY (ExamID) REFERENCES Exams(ExamID)
        )
        """)
        print("Таблица 'Grades' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Grades': {err}")

create_tables()

def NumberOfStrochka(table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    return row_count

def RandomAVERYTHING():
    Names = ["Alpha", "Beta", "Gamma", "Delta", "Zeta", "Teta", "Lambda", "Sigma", "REAL Sigma"]
    Surnames = ["Andrewev", "Andreyev", "Andreiev", "Andoreiev", "Alalodreyev", "_☺§_+ev", "Androidev", "Iphonev", "Linuxev"]
    Birthdates = ["1990-01-01", "1980-02-02", "1970-03-03", "1960-04-04", "1950-05-05", "1940-06-06", "1930-07-07", "1920-08-08", "1940-09-09", "2000-01-01", "2008-10-16", "1950-10-10", "1960-11-12"]
    Departments = ["First", "Second", "Third", "Fourth", "Fifth"]
    CourseNames = ["Math", "Physics", "Chemistry", "Biology", "English", "Russian", "German", "French", "Italian"]
    DepartmentNames = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry", "Engineering", "Psychology", "History", "Economics", "Sociology"]

    for _ in range(random.randint(200, 500)):
        cursor.execute("""
        INSERT INTO Students (Name, Surname, DateOfBirth, Department)
        VALUES (?, ?, ?, ?)""", 
        (random.choice(Names), random.choice(Surnames), random.choice(Birthdates), random.choice(Departments)))

    for _ in range(random.randint(30, 100)):
        cursor.execute("""
        INSERT INTO Teachers (Name, Surname, Department)
        VALUES (?, ?, ?)""", 
        (random.choice(Names), random.choice(Surnames), random.choice(DepartmentNames)))
    
    for _ in range(random.randint(10, 20)):
        cursor.execute("""
        INSERT INTO Courses (Title, Description, TeacherID)
        VALUES (?, ?, ?)""", 
        (random.choice(CourseNames), "Description for " + random.choice(CourseNames), random.randint(1, NumberOfStrochka("Teachers"))))
    
    for _ in range(random.randint(20, 100)):
        cursor.execute("""
        INSERT INTO Exams (ExamDate, MaxScore, CourseID)
        VALUES (?, ?, ?)""", 
        (random.choice(Birthdates), random.randint(110, 120), random.randint(1, NumberOfStrochka("Courses"))))
    
    for _ in range(random.randint(100, 200)):
        cursor.execute("""
        INSERT INTO Grades (StudentID, ExamID, Score)
        VALUES (?, ?, ?)""", 
        (random.randint(1, NumberOfStrochka("Students")), random.randint(1, NumberOfStrochka("Exams")), random.randint(1, 100)))

    db_connection.commit()

RandomAVERYTHING()

def AddToStudents():
    insert = "INSERT INTO Students (Name, Surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)"
    to_insert = [(input("Введите имя студента: "), 
                  input("Введите фамилию студента: "), 
                  input("Введите факультет студента: "), 
                  input("Введите дату рождения студента (YYYY-MM-DD): "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Students'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Students': {err}")

def AddToTeachers():
    insert = "INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)"
    to_insert = [(input("Введите имя преподавателя: "), 
                  input("Введите фамилию преподавателя: "), 
                  input("Введите кафедру преподавателя: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Teachers'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Teachers': {err}")

def AddToCourses():
    insert = "INSERT INTO Courses (Title, Description, TeacherID) VALUES (?, ?, ?)"
    to_insert = [(input("Введите название курса: "), 
                  input("Введите описание курса: "), 
                  int(input("Введите ID преподавателя: ")))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"{cursor.rowcount} записей успешно добавлены в таблицу 'Courses'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Courses': {err}")

# №2

def UpdateStudent():
    student_id = int(input("Введите ID студента для обновления: "))
    new_name = input("Введите новое имя (оставьте пустым, если не хотите менять): ")
    new_surname = input("Введите новую фамилию (оставьте пустым, если не хотите менять): ")
    new_department = input("Введите новый факультет (оставьте пустым, если не хотите менять): ")
    new_date_of_birth = input("Введите новую дату рождения (YYYY-MM-DD) (оставьте пустым, если не хотите менять): ")

    updates = []
    params = []
    
    if new_name:
        updates.append("Name = ?")
        params.append(new_name)
    if new_surname:
        updates.append("Surname = ?")
        params.append(new_surname)
    if new_department:
        updates.append("Department = ?")
        params.append(new_department)
    if new_date_of_birth:
        updates.append("DateOfBirth = ?")
        params.append(new_date_of_birth)

    if updates:
        update_query = f"UPDATE Students SET {', '.join(updates)} WHERE StudentID = ?"
        params.append(student_id)

        try:
            cursor.execute(update_query, params)
            db_connection.commit()
            print(f"Студент с ID {student_id} успешно обновлен.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении студента: {err}")
    else:
        print("Нет данных для обновления.")

def UpdateTeacher():
    teacher_id = int(input("Введите ID преподавателя для обновления: "))
    new_name = input("Введите новое имя (оставьте пустым, если не хотите менять): ")
    new_surname = input("Введите новую фамилию (оставьте пустым, если не хотите менять): ")
    new_department = input("Введите новую кафедру (оставьте пустым, если не хотите менять): ")

    updates = []
    params = []
    
    if new_name:
        updates.append("Name = ?")
        params.append(new_name)
    if new_surname:
        updates.append("Surname = ?")
        params.append(new_surname)
    if new_department:
        updates.append("Department = ?")
        params.append(new_department)

    if updates:
        update_query = f"UPDATE Teachers SET {', '.join(updates)} WHERE TeacherID = ?"
        params.append(teacher_id)

        try:
            cursor.execute(update_query, params)
            db_connection.commit()
            print(f"Преподаватель с ID {teacher_id} успешно обновлен.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении преподавателя: {err}")
    else:
        print("Нет данных для обновления.")

def UpdateCourse():
    course_id = int(input("Введите ID курса для обновления: "))
    new_title = input("Введите новое название курса (оставьте пустым, если не хотите менять): ")
    new_description = input("Введите новое описание курса (оставьте пустым, если не хотите менять): ")
    new_teacher_id = input("Введите новый ID преподавателя (оставьте пустым, если не хотите менять): ")

    updates = []
    params = []
    
    if new_title:
        updates.append("Title = ?")
        params.append(new_title)
    if new_description:
        updates.append("Description = ?")
        params.append(new_description)
    if new_teacher_id:
        updates.append("TeacherID = ?")
        params.append(int(new_teacher_id))

    if updates:
        update_query = f"UPDATE Courses SET {', '.join(updates)} WHERE CourseID = ?"
        params.append(course_id)

        try:
            cursor.execute(update_query, params)
            db_connection.commit()
            print(f"Курс с ID {course_id} успешно обновлен.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении курса: {err}")
    else:
        print("Нет данных для обновления.")

# №3
def DeleteStudent():
    student_id = int(input("Введите ID студента для удаления: "))
    try:
        cursor.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Студент с ID {student_id} успешно удален.")
        else:
            print(f"Студент с ID {student_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении студента: {err}")

def DeleteTeacher():
    teacher_id = int(input("Введите ID преподавателя для удаления: "))
    try:
        cursor.execute("DELETE FROM Teachers WHERE TeacherID = ?", (teacher_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Преподаватель с ID {teacher_id} успешно удален.")
        else:
            print(f"Преподаватель с ID {teacher_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении преподавателя: {err}")

def DeleteCourse():
    course_id = int(input("Введите ID курса для удаления: "))
    try:
        cursor.execute("DELETE FROM Courses WHERE CourseID = ?", (course_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Курс с ID {course_id} успешно удален.")
        else:
            print(f"Курс с ID {course_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении курса: {err}")

def DeleteExam():
    exam_id = int(input("Введите ID экзамена для удаления: "))
    try:
        cursor.execute("DELETE FROM Exams WHERE ExamID = ?", (exam_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Экзамен с ID {exam_id} успешно удален.")
        else:
            print(f"Экзамен с ID {exam_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении экзамена: {err}")

update_option = input("Хотите обновить информацию? (yes/no): ").lower()
if update_option == 'yes':
    while True:
        update_choice = input("Что вы хотите обновить? (Students/Teachers/Courses/exit): ").lower()
        if update_choice == "students":
            UpdateStudent()
        elif update_choice == "teachers":
            UpdateTeacher()
        elif update_choice == "courses":
            UpdateCourse()
        elif update_choice == "exit":
            break
        else:
            print("Неверный выбор.")

delete_option = input("Хотите удалить информацию? (yes/no): ").lower()
if delete_option == 'yes':
    while True:
        delete_choice = input("Что вы хотите удалить? (Students/Teachers/Courses/Exams/exit): ").lower()
        if delete_choice == "students":
            DeleteStudent()
        elif delete_choice == "teachers":
            DeleteTeacher()
        elif delete_choice == "courses":
            DeleteCourse()
        elif delete_choice == "exams":
            DeleteExam()
        elif delete_choice == "exit":
            break
        else:
            print("Неверный выбор.")

# №4

def GetStudentsByDepartment():
    department = input("Введите название факультета для получения списка студентов: ")
    cursor.execute("SELECT * FROM Students WHERE Department = ?", (department,))
    students = cursor.fetchall()

    if students:
        print(f"Студенты факультета '{department}':")
        for student in students:
            print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Дата рождения: {student[4]}")
    else:
        print(f"Нет студентов на факультете '{department}'.")

# №5

def GetCoursesByTeacher():
    teacher_id = int(input("Введите ID преподавателя для получения списка курсов: "))
    cursor.execute("SELECT * FROM Courses WHERE TeacherID = ?", (teacher_id,))
    courses = cursor.fetchall()

    if courses:
        print(f"Курсы, читаемые преподавателем с ID {teacher_id}:")
        for course in courses:
            print(f"ID: {course[0]}, Название: {course[1]}, Описание: {course[2]}")
    else:
        print(f"Нет курсов, читаемых преподавателем с ID {teacher_id}.")

# №6

def GetStudentsByCourse():
    course_id = int(input("Введите ID курса для получения списка студентов: "))
    cursor.execute("""
    SELECT Students.StudentID, Students.Name, Students.Surname, Students.Birthdate
    FROM Students 
    INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID 
    WHERE Enrollments.CourseID =?""", (course_id,))
    students = cursor.fetchall()

    if students:
        print(f"Студенты, изучающие курс с ID {course_id}:")
        for student in students:
            print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Дата рождения: {student[3]}")
    else:
        print(f"Нет студентов, изучающих курс с ID {course_id}.")

# №7

def GetStudentsScoreByCourse():
    course_id = int(input("Введите ID курса для получения списка студентов с их баллами: "))
    cursor.execute("""
    SELECT Students.StudentID, Students.Name, Students.Surname, Students.Birthdate, Grades.Score 
    FROM Students 
    INNER JOIN Grades ON Students.StudentID = Grades.StudentID 
    WHERE Grades.CourseID =?""", (course_id,))
    students = cursor.fetchall()

# №8

def GetStudentAverageCourseScore():
    student_id = int(input("Введите ID студента для получения среднего балла: "))
    course_id = int(input("Введите ID курса для получения среднего балла: "))
    try:
        cursor.execute("""
        SELECT avg(Score) AS AverageScore
        FROM Grades g
        JOIN Exams e ON g.ExamID = e.ExamID
        JOIN Courses c ON e.CourseID = c.CourseID
        WHERE g.StudentID = ? AND c.CourseID = ?""", (student_id, course_id))
        
        result = cursor.fetchone()
        average_score = result[0] if result[0] is not None else 0
        print(f"Средний балл студента с ID {student_id} по курсу с ID {course_id}: {average_score:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")

# №9

def GetStudentAverageScore():
    student_id = int(input("Введите ID студента для получения среднего балла в целом: "))
    try:
        cursor.execute("""
        SELECT avg(Score) AS AverageScore
        FROM Grades
        WHERE StudentID = ?""", (student_id,)) 
        result = cursor.fetchone()
        overall_average = result[0] if result[0] is not None else 0
        print(f"Средний балл студента с ID {student_id} в целом: {overall_average:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")

# №10

def GetDepartmentAverageScore():
    department = input("Введите название факультета для получения среднего балла: ")
    try:
        cursor.execute("""
        SELECT avg(Score) AS AverageScore
        FROM Grades
        JOIN Students ON Grades.StudentID = Students.StudentID
        JOIN Courses ON Grades.CourseID = Courses.CourseID
        WHERE Students.Department = ?""", (department,))
        
        result = cursor.fetchone()
        department_average = result[0] if result[0] is not None else 0
        print(f"Средний балл в целом по факультету '{department}': {department_average:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")

def AddToTable(table_name):
    if table_name == "Students":
        AddToStudents()
    elif table_name == "Teachers":
        AddToTeachers()
    elif table_name == "Courses":
        AddToCourses()

db_connection.close()