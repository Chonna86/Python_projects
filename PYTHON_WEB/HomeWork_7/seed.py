from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random
from datetime import date, timedelta

fake = Faker()

engine = create_engine('postgresql://postgres:password@localhost/postgres')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def seed_data():
    # Seed groups
    group_names = ['Group A', 'Group B', 'Group C']
    groups = [Group(name=name) for name in group_names]
    session.add_all(groups)
    session.commit()

    # Seed teachers
    teacher_names = ['Teacher 1', 'Teacher 2', 'Teacher 3']
    teachers = [Teacher(name=name) for name in teacher_names]
    session.add_all(teachers)
    session.commit()

    # Seed subjects
    subject_names = ['Math', 'Science', 'History', 'English']
    subjects = [Subject(name=name, teacher=random.choice(teachers)) for name in subject_names]
    session.add_all(subjects)
    session.commit()

    # Seed students
    for _ in range(30):
        student = Student(fullname=fake.name(), group=random.choice(groups))
        session.add(student)
        session.commit()

    # Seed grades
    for student in session.query(Student).all():
        for subject in subjects:
            for _ in range(random.randint(5, 20)):
                grade = Grade(value=random.uniform(60, 100), date=fake.date_between(start_date='-1y', end_date='today'), student=student, subject=subject)
                session.add(grade)
    session.commit()


if __name__ == '__main__':
    seed_data()