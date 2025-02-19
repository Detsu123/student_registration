# grade.py
class Grade:
    def __init__(self):
        self.grades = {}  # Dictionary to store grades {student_id: {course_id: grade}}

    def add_grade(self, student_id, course_id, grade):
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][course_id] = grade

    def list_grades(self, student_id):
        if student_id in self.grades:
            print(f"\nGrades for Student ID: {student_id}")
            for course_id, grade in self.grades[student_id].items():
                print(f"Course ID: {course_id}, Grade: {grade}")
        else:
            print(f"No grades found for Student ID: {student_id}")
