import csv
import utils.constants as constants

class csv_file_mange:
    @staticmethod
    def save_courses_to_csv(courses):
        with open(constants.COURSES_CSV_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            for course in courses:
                writer.writerow([course])

    @staticmethod
    def load_courses_from_csv():
        courses = []
        try:
            with open(constants.COURSES_CSV_PATH, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    courses.append(row[0])
        except FileNotFoundError:
            pass
        return courses