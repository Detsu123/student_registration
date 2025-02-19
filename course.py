# course.py
class Course:
    def __init__(self, course_id, course_name, credit_hours):
        self.course_id = course_id
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"
