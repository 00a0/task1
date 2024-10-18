import sqlite3
import random

db_connection = sqlite3.connect('task1.db')
cursor = db_connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

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
            FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE
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
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
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
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
            FOREIGN KEY (ExamID) REFERENCES Exams(ExamID) ON DELETE CASCADE
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

def RandomBirthDate():
    year = random.randint(1950, 2002)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return date

def RandomExamDate():
    year = random.randint(2021, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return date

def RandomAVERYTHING():
    Names = ["Alpha", "Beta", "Gamma", "Delta", "Zeta", "Teta", "Lambda", "Sigma", "REAL Sigma"]
    Surnames = ["Andrewev", "Andreyev", "Andreiev", "Andoreiev", "Alalodreyev", "_☺§_+ev", "Androidev", "Iphonev", "Linuxev"]
    Birthdates = []
    ExamDates = []
    for i in range(3000):
        Birthdates.append(RandomBirthDate())
    for i in range(1000):
        ExamDates.append(RandomExamDate())
    Departments = ["First", "Second", "Third", "Fourth", "Fifth"]
    CourseNames = ["Math", "Physics", "Chemistry", "Biology", "English", "Russian", "German", "French", "Italian"]
    DepartmentNames = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry", "Engineering", "Psychology", "History", "Economics", "Sociology"]

    for i in range(random.randint(150, 200)):
        cursor.execute("""
        INSERT INTO Students (Name, Surname, DateOfBirth, Department)
        VALUES (?, ?, ?, ?)""", 
        (random.choice(Names), random.choice(Surnames), random.choice(Birthdates), random.choice(Departments)))

    for i in range(random.randint(10, 20)):
        cursor.execute("""
        INSERT INTO Teachers (Name, Surname, Department)
        VALUES (?, ?, ?)""", 
        (random.choice(Names), random.choice(Surnames), random.choice(DepartmentNames)))
    
    for i in range(random.randint(NumberOfStrochka("Teachers")//2 , NumberOfStrochka("Teachers"))):
        course_name = random.choice(CourseNames)
        cursor.execute("""
        INSERT INTO Courses (Title, Description, TeacherID)
        VALUES (?, ?, ?)""", 
        (course_name, "Description for " + course_name, random.randint(1, NumberOfStrochka("Teachers"))))
    
    for i in range(random.randint(450, 500)):
        cursor.execute("""
        INSERT INTO Exams (ExamDate, MaxScore, CourseID)
        VALUES (?, ?, ?)""", 
        (random.choice(ExamDates), random.randint(101, 110), random.randint(1, NumberOfStrochka("Courses"))))
    
    for i in range(NumberOfStrochka("Exams")):
        cursor.execute("""
        INSERT INTO Grades (StudentID, ExamID, Score)
        VALUES (?, ?, ?)""", 
        (random.randint(1, NumberOfStrochka("Students")), random.randint(1, NumberOfStrochka("Exams")), random.randint(40, 100)))

    db_connection.commit()

RandomAVERYTHING()

def AddStudent():
    insert = "INSERT INTO Students (Name, Surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)"
    to_insert = [(input("Введите имя студента: "), 
                  input("Введите фамилию студента: "), 
                  input("Введите факультет студента: "), 
                  input("Введите дату рождения студента (YYYY-MM-DD): "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Students'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Students': {err}")

def AddTeacher():
    insert = "INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)"
    to_insert = [(input("Введите имя преподавателя: "), 
                  input("Введите фамилию преподавателя: "), 
                  input("Введите кафедру преподавателя: "))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Teachers'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Teachers': {err}")

def AddCourse():
    insert = "INSERT INTO Courses (Title, Description, TeacherID) VALUES (?, ?, ?)"
    to_insert = [(input("Введите название курса: "), 
                  input("Введите описание курса: "), 
                  int(input("Введите ID преподавателя: ")))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Courses'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Courses': {err}")

def AddExam():
    insert = "INSERT INTO Exams (ExamDate, CourseID, MaxScore) VALUES (?, ?, ?)"
    to_insert = [(input("Введите дату экзамена (YYYY-MM-DD): "),
                  int(input("Введите ID курса: ")),
                  int(input("Введите максимальный балл экзамена: ")))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Exams'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Exams': {err}")

def AddGrade():
    insert = "INSERT INTO Grades (StudentID, ExamID, Score) VALUES (?,?, ?)"
    to_insert = [(int(input("Введите ID студента: ")),
                  int(input("Введите ID экзамена: ")),
                  int(input("Введите оценку: ")))]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Grades'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Grades': {err}")

# №2

def UpdateStudent():
    try:
        student_id = int(input("Введите ID студента для обновления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
        student_id = int(input("Введите ID преподавателя для обновления: "))
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
    try:
        teacher_id = int(input("Введите ID преподавателя для обновления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
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
    try:
        course_id = int(input("Введите ID курса для обновления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
        course_id = int(input("Введите ID преподавателя для обновления: "))
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
    try:
        student_id = int(input("Введите ID студента для удаления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
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
    try:
        teacher_id = int(input("Введите ID преподавателя для удаления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
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
    try:
        course_id = int(input("Введите ID курса для удаления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
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
    try:
        exam_id = int(input("Введите ID экзамена для удаления: "))
    except ValueError:
        print("Вводите ID числом, пожалуйста")
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

def Update():
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

def Delete():
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

def Add():
    while True:
        add_choice = input("Что вы хотите добавить? (Students/Teachers/Courses/Exams/Grades/exit): ").lower()
        
        if add_choice == "students":
            AddStudent()
        elif add_choice == "teachers":
            AddTeacher()
        elif add_choice == "courses":
            AddCourse()
        elif add_choice == "exams":
            AddExam()
        elif add_choice == "grades":
            AddGrade()
        elif add_choice == "exit":
            break
        else:
            print("Неверный выбор.")

# №4

def GetStudentsByDepartment():
    department = input("Введите название факультета для получения списка студентов: ")
    try:
        cursor.execute("SELECT * FROM Students WHERE Department = ?", (department,))
        students = cursor.fetchall()

        if students:
            print(f"Студенты факультета '{department}':")
            for student in students:
                print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Дата рождения: {student[4]}")
        else:
            print(f"Нет студентов на факультете '{department}'.")
    except:
        print("Ошибка при получении студентов факультета.")

# №5

def GetCoursesByTeacher():
    teacher_id = int(input("Введите ID преподавателя для получения списка курсов: "))
    try:
        cursor.execute("SELECT * FROM Courses WHERE TeacherID = ?", (teacher_id,))
        courses = cursor.fetchall()

        if courses:
            print(f"Курсы, читаемые преподавателем с ID {teacher_id}:")
            for course in courses:
                print(f"ID: {course[0]}, Название: {course[1]}, Описание: {course[2]}")
        else:
            print(f"Нет курсов, читаемых преподавателем с ID {teacher_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении курсов преподавателем: {err}")

# №6

def GetStudentsByCourse():
    course_id = int(input("Введите ID курса для получения списка студентов: "))
    try:
        cursor.execute("""
        SELECT Students.StudentID, Students.Name, Students.Surname, Students.DateOfBirth
        FROM Students 
        JOIN Grades ON Students.StudentID = Grades.StudentID 
        JOIN Exams ON Grades.ExamID = Exams.ExamID
        JOIN Courses ON Exams.CourseID = Courses.CourseID
        WHERE Courses.CourseID =?""", (course_id,))
        students = cursor.fetchall()

        if students:
            print(f"Студенты, изучающие курс с ID {course_id}:")
            for student in students:
                print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Дата рождения: {student[3]}")
        else:
            print(f"Нет студентов, изучающих курс с ID {course_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении студентов из курса: {err}")

# №7

def GetStudentsScoreByCourse():
    course_id = int(input("Введите ID курса для получения списка студентов с их баллами: "))
    try:
        cursor.execute("""
        SELECT Students.StudentID, Students.Name, Students.Surname, Students.DateOfBirth, Grades.Score 
        FROM Students 
        JOIN Grades ON Students.StudentID = Grades.StudentID 
        JOIN Exams ON Grades.ExamID = Exams.ExamID
        WHERE Exams.CourseID =?""", (course_id,))
        students = cursor.fetchall()

        if students:
            print(f"Студенты, изучающие курс с ID {course_id} с баллами:")
            for student in students:
                print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Дата рождения: {student[3]}, Балл: {student[4]}")
        else:
            print(f"Нет студентов, изучающих курс с ID {course_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении баллов студентов: {err}")

# №8

def GetStudentAverageCourseScore():
    student_id = int(input("Введите ID студента для получения среднего балла: "))
    course_id = int(input("Введите ID курса для получения среднего балла: "))
    try:
        cursor.execute("""
        SELECT avg(Score) AS AverageScore
        FROM Grades 
        JOIN Exams ON Grades.ExamID = Exams.ExamID
        JOIN Courses ON Exams.CourseID = Courses.CourseID
        WHERE Grades.StudentID = ? AND Courses.CourseID = ?""", (student_id, course_id))
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
        JOIN Exams ON Grades.ExamID = Exams.ExamID
        JOIN Courses ON Exams.CourseID = Courses.CourseID
        WHERE Students.Department = ?""", (department,))
        
        result = cursor.fetchone()
        department_average = result[0] if result[0] is not None else 0
        print(f"Средний балл в целом по факультету '{department}': {department_average:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")

def UserInput():
        print("\n Меню (1/2/3/4/5/6/7/8/9/10/exit):")
        print("1. Добавление нового студента, преподавателя, курса, экзамена и оценки.")
        print("2. Изменение информации о студентах, преподавателях и курсах.")
        print("3. Удаление студентов, преподавателей, курсов и экзаменов.")
        print("4. Получение списка студентов по факультету.")
        print("5. Получение списка курсов, читаемых определенным преподавателем.")
        print("6. Получение списка студентов, зачисленных на конкретный курс.")
        print("7. Получение оценок студентов по определенному курсу.")
        print("8. Средний балл студента по определенному курсу.")
        print("9. Средний балл студента в целом.")
        print("10. Средний балл по факультету.")
        user_answer = input("Введите запрос из Меню: ").lower()
        while user_answer != "exit":         
            match user_answer:
                case "1":
                    Add()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "2":
                    Update()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "3":
                    Delete()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "4":
                    GetStudentsByDepartment()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "5":
                    GetCoursesByTeacher()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "6":
                    GetStudentsByCourse()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "7":
                    GetStudentsScoreByCourse()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "8":
                    GetStudentAverageCourseScore()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "9":
                    GetStudentAverageScore()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case "10":
                    GetDepartmentAverageScore()
                    user_answer = input("Введите запрос из Меню: ").lower()
                case _:
                    print("Некорректный ввод. Попробуйте снова.")
                    user_answer = input("Введите запрос из Меню: ").lower()

print("\nБаза данных была Случайно сгенерированна!")

UserInput()

db_connection.close()