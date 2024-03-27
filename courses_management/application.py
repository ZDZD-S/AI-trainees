from course_registry import CourseRegistry
from csv_file_mange import csv_file_mange
from utils.slack import send_slack_notification
from utils.constants import MenuChoices

class Application:
    def __init__(self):
        self.course_registry = CourseRegistry()
        # Load existing courses from CSV at startup
        courses = csv_file_mange.load_courses_from_csv()
        for course in courses:
            self.course_registry.add_course(course)

    def add_course(self, course_name):
        try:
            self.course_registry.add_course(course_name)
            # Save changes 
            csv_file_mange.save_courses_to_csv(self.course_registry.list_courses())
            print(f"Course '{course_name}' added successfully.")
        except ValueError as e:
            error_message = str(e)
            send_slack_notification(error_message)
            print(error_message)

    def drop_course(self, course_name):
        try:
            self.course_registry.drop_course(course_name)
            # Save changes 
            csv_file_mange.save_courses_to_csv(self.course_registry.list_courses())
            print(f"Course '{course_name}' dropped successfully.")
        except ValueError as e:
            error_message = str(e)
            send_slack_notification(error_message)
            print(error_message)

    def list_courses(self):
        courses = self.course_registry.list_courses()
        if courses:
            print("\nCourses currently enrolled in:")
            for course in courses:
                print(course)
        else:
            print("\nNo courses currently enrolled.")

    def run(self):
        while True:
            print("\nMain Menu")
            for choice in MenuChoices:
                print(f"{choice.value}. {choice.name.replace('_', ' ')}")
            choice_input = input("Enter your choice: ")

            if choice_input == str(MenuChoices.ADD_COURSE.value):
                course_name = input("Enter the course name to add: ")
                self.add_course(course_name)

            elif choice_input == str(MenuChoices.DROP_COURSE.value):
                course_name = input("Enter the course name to drop: ")
                self.drop_course(course_name)

            elif choice_input == str(MenuChoices.LIST_COURSES.value):
                self.list_courses()

            elif choice_input == str(MenuChoices.EXIT.value):
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = Application()
    app.run()
