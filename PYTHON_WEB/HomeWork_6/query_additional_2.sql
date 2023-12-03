WITH last_lesson_date AS (
    SELECT 
        subject_id,
        MAX(date) AS last_lesson_date
    FROM grades
    GROUP BY subject_id
)

SELECT 
    students.name AS student_name,
    grades.grade,
    last_lesson_date.last_lesson_date
FROM grades
JOIN last_lesson_date ON grades.subject_id = last_lesson_date.subject_id AND grades.date = last_lesson_date.last_lesson_date
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE groups.id = "реальний group_id"
    AND grades.subject_id = "реальний subject_id"
ORDER BY last_lesson_date.last_lesson_date DESC;