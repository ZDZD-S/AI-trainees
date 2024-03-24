from course_registry import CourseRegistry
from csv_file_mange import csv_file_mange
from slack import send_slack_notification

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
        except Exception as e:
            error_message = f"Error adding course '{course_name}':\n {str(e)}"
            send_slack_notification(error_message)
            print(error_message)

    def drop_course(self, course_name):
        try:
            self.course_registry.drop_course(course_name)
            # Save changes 
            csv_file_mange.save_courses_to_csv(self.course_registry.list_courses())
            print(f"Course '{course_name}' dropped successfully.")
        except Exception as e:
            error_message = f"Error dropping course '{course_name}':\n {str(e)}"
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
            print("1. Add Course")
            print("2. Drop Course")
            print("3. List Courses")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                course_name = input("Enter the course name to add: ")
                self.add_course(course_name)
            elif choice == '2':
                course_name = input("Enter the course name to drop: ")
                self.drop_course(course_name)
            elif choice == '3':
                self.list_courses()
            elif choice == '4':
                print("Exiting program...")
                break
            else:
                print("Invalid choice, please choose between 1-4.")

if __name__ == "__main__":
    app = Application()
    app.run()
