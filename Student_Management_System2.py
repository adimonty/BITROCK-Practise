#Building a Student Management System

class Student:
    def __init__(self, student_id, first_name, last_name, age, email, phone):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone

class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

def validate_student_course_ids(func):
    def wrapper(self, student_id, course_id):
        if student_id not in self.students or course_id not in self.courses:
            raise ValueError("Invalid student ID or course ID.")
        return func(self, student_id, course_id)
    return wrapper

class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary that stores students with student_id as key
        self.courses = {}   # Dictionary that stores courses with course_id as key
        self.enrollments = []  # List that stores enrollment information as a tuple (student_id, course_id)

    def add_student(self, student_id, first_name, last_name, age, email, phone):
        if student_id in self.students:
            raise ValueError("Student ID already exists. Please use a different ID.")
        student = Student(student_id, first_name, last_name, age, email, phone)
        self.students[student_id] = student

    def add_course(self, course_id, course_name, credits):
        if course_id in self.courses:
            raise ValueError("Course ID already exists. Please use a different ID.")
        course = Course(course_id, course_name, credits)
        self.courses[course_id] = course

    @validate_student_course_ids
    def enroll_student(self, student_id, course_id):
        self.enrollments.append((student_id, course_id))

    def _get_students_generator(self):
        for student in self.students.values():
            yield student

    def _get_courses_generator(self):
        for course in self.courses.values():
            yield course

    def get_students_lazy(self):
        return self._get_students_generator()

    def get_courses_lazy(self):
        return self._get_courses_generator()

    def get_student_by_id(self, student_id):
        return self.students.get(student_id)

    def get_course_by_id(self, course_id):
        return self.courses.get(course_id)

    def get_students(self):
        return list(self.students.values())

    def get_courses(self):
        return list(self.courses.values())

    def get_enrollments(self):
        return self.enrollments

# Examples
if __name__ == "__main__":
    try:
        sms = StudentManagementSystem()

        sms.add_student(1, "John", "Doe", 20, "john@example.com", "1234567890")
        sms.add_student(2, "Jane", "Smith", 22, "jane@example.com", "9876543210")

        sms.add_course(1, "Maths", 6)
        sms.add_course(2, "Chemistry", 3)

        sms.enroll_student(1, 1)  # John enrolls in Maths
        sms.enroll_student(2, 1)  # Jane enrolls in Maths
        sms.enroll_student(2, 2)  # Jane enrolls in Physics

        # Retrieve data using generators
        print("Students:")
        for student in sms.get_students_lazy():
            print(f"{student.first_name} {student.last_name} (ID: {student.student_id})")

        print("\nCourses:")
        for course in sms.get_courses_lazy():
            print(f"{course.course_name} (ID: {course.course_id})")

        print("\nEnrollments:")
        for enrollment in sms.get_enrollments():
            student_id, course_id = enrollment
            student = sms.get_student_by_id(student_id)
            course = sms.get_course_by_id(course_id)
            print(f"{student.first_name} {student.last_name} enrolls in {course.course_name}")

    except ValueError as e:
        print(f"Error: {e}")
