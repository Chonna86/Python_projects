from sqlalchemy import func, desc
from models import Student, Grade, Group, Subject, Teacher
from sqlalchemy.orm import sessionmaker

def select_1(session):
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    query = session.query(Student.fullname, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5)
    return query.all()

def select_2(session):
    # Знайти студента із найвищим середнім балом з певного предмета.
    query = session.query(Student.fullname, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == 'subject_name') \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(1)
    return query.first()

def select_3(session):
    # Знайти середній бал у групах з певного предмета.
    query = session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Student, Group.id == Student.group_id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == 'subject_name') \
        .group_by(Group.id)
    return query.all()

def select_4(session):
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade'))
    return query.first()

def select_5(session):
    # Знайти які курси читає певний викладач.
    query = session.query(Subject.name) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == 'teacher_name')
    return query.all()

def select_6(session, group_name):
    # Знайти список студентів у певній групі.
    query = session.query(Student.fullname) \
        .join(Group, Student.group_id == Group.id) \
        .filter(Group.name == group_name)
    return query.all()

def select_7(session, group_name, subject_name):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    query = session.query(Student.fullname, Grade.value) \
        .join(Group, Student.group_id == Group.id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Group.name == group_name, Subject.name == subject_name)
    return query.all()

def select_8(session, teacher_name):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == teacher_name)
    return query.first()

def select_9(session, student_name):
    # Знайти список курсів, які відвідує певний студент.
    query = session.query(Subject.name) \
        .join(Grade, Subject.id == Grade.subject_id) \
        .join(Student, Grade.student_id == Student.id) \
        .filter(Student.fullname == student_name)
    return query.all()

def select_10(session, student_name, teacher_name):
    # Список курсів, які певному студенту читає певний викладач.
    query = session.query(Subject.name) \
        .join(Grade, Subject.id == Grade.subject_id) \
        .join(Student, Grade.student_id == Student.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.fullname == student_name, Teacher.name == teacher_name)
    return query.all()