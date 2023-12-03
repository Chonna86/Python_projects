SELECT 
    teachers.name AS teacher_name,
    students.name AS student_name,
    AVG(grades.grade) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE teachers.id = "реальний teacher_id"
    AND students.id = "реальний student_id"
GROUP BY teachers.name, students.name;