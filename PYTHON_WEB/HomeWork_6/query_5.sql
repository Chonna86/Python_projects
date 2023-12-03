SELECT subjects.name
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
WHERE teachers.name = "ім'я викладача";