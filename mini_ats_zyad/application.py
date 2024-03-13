from add_job import job
from register_candidate import candidate

# Defines the main function where the program starts
def main():

    while True:
        # Display the menu options
        print("\nSimple ATS")
        print("1. Add job")
        print("2. Register candidate")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            # Option to add a new job
            title = input("Title: ")  
            description = input("Description: ")  
            job = job(title, description) 
            job.save() 
        elif choice == "2":
            # Option to register a new candidate
            name = input("Name: ")
            phonenumber = input("Phone Number: ")
            email = input("Email: ")
            candidate = candidate(name, phonenumber, email)
            candidate.save()  
        elif choice == "3":
            # Option to exit the application
            print("Exiting...")
            break  # Breaks the loop, ending the program
        else:
            # Handles invalid menu choices
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    main()