import psycopg2
from psycopg2 import sql
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker()

def populate_tables():
    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='password')
    cursor = conn.cursor()

    try:
        # Наповнення groups
        for _ in range(3):
            cursor.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))

        # Наповнення teachers
        for _ in range(3):
            cursor.execute("INSERT INTO teachers (name) VALUES (%s)", (fake.name(),))

        # Наповнення students
        for _ in range(30):
            cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (fake.name(), random.randint(1, 3)))

        # Наповнення subjects
        for _ in range(5):
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (fake.word(), random.randint(1, 3)))

        # Наповнення grades
        for student_id in range(1, 31):
            for subject_id in range(1, 6):
                for _ in range(20):
                    cursor.execute(
                        "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)",
                        (student_id, subject_id, random.randint(1, 100), fake.date_this_decade())
                    )

        conn.commit()
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    populate_tables()
 