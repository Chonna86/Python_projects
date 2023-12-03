SELECT students.name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 'ID предмета'
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;