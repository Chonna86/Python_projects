SELECT subjects.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = "ім'я студента" AND teachers.name = "ім'я викладача";