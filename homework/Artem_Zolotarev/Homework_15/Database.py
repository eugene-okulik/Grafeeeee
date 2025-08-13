import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor()
cursor.execute("INSERT INTO students (name, second_name) VALUES ('artem2', 'zolotarev2')")
student_id = cursor.lastrowid

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Basic python', {student_id})")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Typical Python', 'Aug2025', 'Jan2026')")
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students s SET s.group_id = {group_id} WHERE s.id = {student_id})")

cursor.execute("INSERT INTO subjects (title) VALUES ('OOP')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Manual testing')")
subject2_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Auto_testing')")
subject3_id = cursor.lastrowid

cursor.execute(f"INSERT INTO lessons (title, subject1_id) VALUES ('theory', {subject1_id})")
lesson1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('practice', {subject1_id})")
lesson2_id = cursor.lastrowid
cursor.execute(f"fINSERT INTO lessons (title, subject_id) VALUES ('test-case', {subject2_id})")
lesson3_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('bag-repots', {subject2_id})")
lesson4_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('kibana', {subject3_id})")
lesson5_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('grafana', {subject3_id})")
lesson6_id = cursor.lastrowid

lst_values = [(5, lesson6_id, student_id),
              (4, lesson5_id, student_id),
              (3, lesson4_id, student_id),
              (2, lesson3_id, student_id),
              (2, lesson2_id, student_id),
              (3, lesson1_id, student_id)
              ]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", lst_values)

cursor.execute(f"SELECT marks.value FROM marks WHERE marks.student_id = {student_id}")
data = cursor.fetchall()
print(data)

cursor.execute(f"SELECT title FROM books WHERE books.taken_by_student_id = {student_id}")
data = cursor.fetchall()
print(data)

cursor.execute(
    "SELECT s.name, s.second_name, g.title, b.title, m.value, l.title, s2.title "
    "FROM students s "
    "JOIN `groups` g ON g.id = s.group_id "
    "JOIN books b ON b.taken_by_student_id = s.id "
    "JOIN marks m ON m.student_id = s.id "
    "JOIN lessons l ON l.id = m.lesson_id "
    "JOIN subjects s2 ON s2.id = l.subject_id "
    f"WHERE s.id = {student_id} "
)
data = cursor.fetchall()
for line in data:
    print(line)

db.close()
