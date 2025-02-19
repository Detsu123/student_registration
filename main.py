# main.py
from student import Student
from course import Course
from registration import Registration
from grade import Grade

def main():
    registration = Registration()
    grades = Grade()

    # Sample data
    student1 = Student("S001", "John Doe", 20)
    student2 = Student("S002", "Jane Smith", 22)
    course1 = Course("C101", "Mathematics", 3)
    course2 = Course("C102", "Physics", 4)

    # Add students and courses
    registration.add_student(student1)
    registration.add_student(student2)
    registration.add_course(course1)
    registration.add_course(course2)

    # Add grades
    grades.add_grade("S001", "C101", "A")
    grades.add_grade("S001", "C102", "B")
    grades.add_grade("S002", "C101", "A+")

    # Display all registered students and courses
    registration.list_students()
    registration.list_courses()

    # Display grades for a student
    grades.list_grades("S001")

if __name__ == "__main__":
    main()
