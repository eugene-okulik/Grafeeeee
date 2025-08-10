import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor()
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('artem2', 'zolotarev2'))

cursor.execute("INSERT INTO books (title, taken_by_student_id) "
               "VALUES (%s, %s)", ('Basic python', 20963))

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('Typical Python', 'Aug2025', 'Jan2026'))

cursor.execute("UPDATE students s SET s.group_id = %s WHERE s.id = 20963", (5521,))

cursor.execute("INSERT INTO subjects (title) VALUES (%s), (%s), (%s) ",
               ('OOP', 'Manual testing', 'Auto_testing'))

cursor.execute("INSERT INTO lessons (title, subject_id) "
               "VALUES (%s, %s), (%s, %s)", ('theory', 11673, 'practice', 11673))

cursor.execute("INSERT INTO lessons (title, subject_id) "
               "VALUES (%s, %s), (%s, %s)", ('test-case', 11674, 'bag-repots', 11674))

cursor.execute("INSERT INTO lessons (title, subject_id) "
               "VALUES (%s, %s), (%s, %s)", ('kibana', 11675, 'grafana', 11675))

lst_values = [(5, 11775, 20963),
              (4, 11774, 20963),
              (3, 11773, 20963),
              (2, 11772, 20963),
              (2, 11771, 20963),
              (3, 11770, 20963)
              ]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", lst_values)
db.commit()

cursor.execute("SELECT marks.value FROM marks WHERE marks.student_id = 20963")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT title FROM books WHERE books.taken_by_student_id = 20963")
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
    "WHERE s.id = 20963 "
)
data = cursor.fetchall()
for line in data:
    print(line)

db.close()
