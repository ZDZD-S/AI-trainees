from add_job import job
from register_candidate import candidate
from utils.constants import APPLICATION_TITLE, MENU_OPTIONS, PROJECT_STATUS, MAX_PHONE_NUMBER_LENGTH, MENU_CHOICE
from utils.errors import (
    EMPTY_INPUT_ERROR, INVALID_EMAIL_ERROR, INVALID_PHONE_NUMBER_ERROR,
    INVALID_LINKEDIN_URL_ERROR, INVALID_SALARY_RANGE_ERROR
)
# Drives the job and candidate management system, handling user interactions for adding jobs and candidates, and enforcing input validation.


def main():
    while True:
        print(f"\\n{APPLICATION_TITLE}")
        for option, description in MENU_OPTIONS.items():
            print(f"{option}. {description}")
        choice = input("Enter choice: ")

        # Process job entry with validation.
        if choice == MENU_CHOICE['Add job']:
            title = input("Title: ").strip()
            while not title:
                print(EMPTY_INPUT_ERROR)
                title = input("Title: ").strip()

            department = input("Department: ").strip()
            while not department:
                print(EMPTY_INPUT_ERROR)
                department = input("Department: ").strip()

            job_type = input("Job type: ").strip()
            while not job_type:
                print(EMPTY_INPUT_ERROR)
                job_type = input("Job type: ").strip()

            description = input("Description: ").strip()
            while not description:
                print(EMPTY_INPUT_ERROR)
                description = input("Description: ").strip()

            requirements = input("Requirements: ").strip()
            while not requirements:
                print(EMPTY_INPUT_ERROR)
                requirements = input("Requirements: ").strip()

            salary_range = input("Salary range (e.g., 8000-10000): ").strip()
            # Basic validation for salary range format
            while "-" not in salary_range or not all(part.isdigit() for part in salary_range.split('-')):
                print(INVALID_SALARY_RANGE_ERROR)
                salary_range = input(
                    "Salary range (e.g., 8000-10000): ").strip()
            # Validation for project status it is [open, closed, completed] format
            print("Current status options:", ', '.join(PROJECT_STATUS))
            current_status = input("Current status: ").strip()
            while current_status not in PROJECT_STATUS:
                print(
                    f"Invalid status. Choose from: {', '.join(PROJECT_STATUS)}")
                current_status = input("Current status: ").strip()

            Job = job(title, department, job_type, description,
                      requirements, salary_range, current_status)
            Job.save()
        # Process candidate entry with validation.
        elif choice == MENU_CHOICE['Register candidate']:
            first_name = input("First Name: ").strip()
            while not first_name:
                print(EMPTY_INPUT_ERROR)
                first_name = input("First Name: ").strip()

            last_name = input("Last Name: ").strip()
            while not last_name:
                print(EMPTY_INPUT_ERROR)
                last_name = input("Last Name: ").strip()
            # Validation for a phone number It is composed 10 numbers format
            phone_number = input("Phone Number: ").strip()
            while not (phone_number.isdigit() and len(phone_number) <= MAX_PHONE_NUMBER_LENGTH):
                print(INVALID_PHONE_NUMBER_ERROR.format(
                    length=MAX_PHONE_NUMBER_LENGTH))
                phone_number = input("Phone Number: ").strip()
            # Validation for right writing an email
            email = input("Email: ").strip()
            while "@" not in email or "." not in email:
                print(INVALID_EMAIL_ERROR)
                email = input("Email: ").strip()

            address = input("Address: ").strip()
            while not address:
                print(EMPTY_INPUT_ERROR)
                address = input("Address: ").strip()
            # Validation for right writing a LinkedIn URL
            linkedin_profile = input("LinkedIn URL: ").strip()
            while not linkedin_profile.startswith("https://www.linkedin.com/"):
                print(INVALID_LINKEDIN_URL_ERROR)
                linkedin_profile = input("LinkedIn URL: ").strip()

            education = input("Education: ").strip()
            while not education:
                print(EMPTY_INPUT_ERROR)
                education = input("Education: ").strip()

            experience = input("Experience: ").strip()
            while not experience:
                print(EMPTY_INPUT_ERROR)
                experience = input("Experience: ").strip()

            skills = input("Skills: ").strip()
            while not skills:
                print(EMPTY_INPUT_ERROR)
                skills = input("Skills: ").strip()

            Candidate = candidate(first_name, last_name, phone_number, email,
                                  address, linkedin_profile, education, experience, skills)
            Candidate.save()

        elif choice == MENU_CHOICE['Exit']:
            print("Exiting...")
            break

        else:
            print("Invalid choice, please choose again.")


if __name__ == '__main__':
    main()
