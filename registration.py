# registration.py
class Registration:
    def __init__(self):
        self.registered_students = []
        self.course_list = []

    def add_student(self, student):
        self.registered_students.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def list_students(self):
        print("\nRegistered Students:")
        for student in self.registered_students:
            print(student)

    def list_courses(self):
        print("\nAvailable Courses:")
        for course in self.course_list:
            print(course)
