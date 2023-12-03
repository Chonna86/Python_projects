import psycopg2
from psycopg2 import sql

def create_tables():
    commands = (
        """
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            group_id INTEGER
        )
        """,
        """
        CREATE TABLE groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        )
        """,
        """
        CREATE TABLE teachers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        )
        """,
        """
        CREATE TABLE subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            teacher_id INTEGER
        )
        """,
        """
        CREATE TABLE grades (
            id SERIAL PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date DATE
        )
        """
    )

    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='password',)
    cursor = conn.cursor()

    try:
        for command in commands:
            cursor.execute(command)
        conn.commit()
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_tables()
    
