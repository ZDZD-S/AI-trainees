from utils.errors import COURSE_ALREADY_EXISTS_ERROR, COURSE_NOT_FOUND_ERROR

class CourseRegistry:
    def __init__(self):
        self.courses = []

    def add_course(self, course_name):
        if course_name in self.courses:
            raise ValueError(COURSE_ALREADY_EXISTS_ERROR.format(course_name=course_name))
        self.courses.append(course_name)

    def drop_course(self, course_name):
        if course_name not in self.courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR.format(course_name=course_name))
        self.courses.remove(course_name)

    def list_courses(self):
        return self.courses
