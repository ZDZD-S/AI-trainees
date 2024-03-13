# Import the csv module
import csv
import os

# Define the list to store course names
courses = []

# Function to display the main menu
def display_menu():
    print("\nMain Menu")
    print("1. Add Course")
    print("2. Drop Course")
    print("3. List Courses")
    print("4. Exit")

# Function to add a course
def add_course():
    course_name = input("Enter the course name to add: ")
    if course_name not in courses:
        courses.append(course_name)
        print(f"Course '{course_name}' added successfully.")
        save_courses_to_csv()
    else:
        print("This course is already in your list.")

# Function to drop a course
def drop_course():
    if not courses:  # Check if the list is empty before dropping
        print("There are no courses added to drop.")
    else:
        course_name = input("Enter the course name to drop: ")
        if course_name in courses:
            courses.remove(course_name)
            print(f"Course '{course_name}' dropped successfully.")
            save_courses_to_csv()
        else:
            print("This course was not found in your list.")

# Function to list courses
def list_courses():
    if not courses:  # Check if the list is empty
        print("There are no courses added.")
    else:
        print("Courses currently enrolled in:")
        for course in courses:
            print(course)

# Function to save courses to a CSV file
def save_courses_to_csv():
    with open('courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for course in courses:
            writer.writerow([course])
    print("Courses saved to courses.csv.")

# Function to load courses from a CSV file
def load_courses_from_csv():
    try:
        with open('courses.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                courses.append(row[0])
    except FileNotFoundError:
        print("No existing course data found. Starting fresh.")
        
# Main program loop
def main():
    load_courses_from_csv()  # Load courses at program startup
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':  # Activate function to add a course
            add_course()
        elif choice == '2':  # Activate function to drop a course
            drop_course()
        elif choice == '3':  # Activate function to list courses
            list_courses()
        elif choice == '4':  
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please choose between 1-4.")

# Hi there (:
main()
