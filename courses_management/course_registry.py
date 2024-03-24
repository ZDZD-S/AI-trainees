from errors import CourseAlreadyExistsError, CourseNotFoundError

class CourseRegistry:
    def __init__(self):
        self.courses = []

    def add_course(self, course_name):
        if course_name in self.courses:
            raise CourseAlreadyExistsError(f"The course '{course_name}' already exists.")
        self.courses.append(course_name)

    def drop_course(self, course_name):
        if course_name not in self.courses:
            raise CourseNotFoundError(f"The course '{course_name}' not found.")
        self.courses.remove(course_name)

    def list_courses(self):
        return self.courses
