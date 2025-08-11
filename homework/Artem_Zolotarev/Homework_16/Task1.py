import csv
import os.path
import dotenv
import mysql.connector as mysql

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
full_path = os.path.join(base_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')


def read_file():
    with open(full_path, newline='') as file:
        data_file = csv.DictReader(file)
        for data_line in data_file:
            yield data_line


def get_query():

    dotenv.load_dotenv()

    db = mysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSW'),
        port=os.getenv('db_port'),
        database=os.getenv('db_name')
    )

    cursor = db.cursor(dictionary=True)
    cursor.execute('''
    SELECT s.name,s.second_name, g.title as group_title, b.title as book_title, s2.title as subject_title, 
    l.title as lesson_title, m.value as mark_value
    FROM students s
    JOIN `groups` g ON g.id = s.group_id
    JOIN books b ON b.taken_by_student_id = s.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s2 ON l.subject_id = s2.id
    WHERE s.name = 'Petr' and s.second_name = 'Ivanov' and g.title = 'GR_O222'
     ''')
    for x in cursor.fetchall():
        yield x

    db.close()


for line in read_file():
    if line not in get_query():
        print(f'{line} нет в бд')
