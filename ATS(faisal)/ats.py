import csv
import os

# Define the path to the CSV file
CSV_FILE = 'jobs.csv'
CSV_FILE1 = 'candidate.csv'

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['title', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Create CSV file1 if it doesn't exist
if not os.path.exists(CSV_FILE1):
    with open(CSV_FILE1, 'w', newline='') as csvfile1:
        fieldnames = ['candidate: name', 'email', 'phone_number']
        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
        writer.writeheader()

# function to candidate list 
def list_candidate():
    with open(CSV_FILE1, 'r', newline='') as csvfile1:
        reader = csv.DictReader(csvfile1)
        candidate = [row for row in reader]
    print("candidate list")
    for candidate in candidate:
        print(f"- {candidate['full_name']}: {candidate['email']}: {candidate['phone_number']}")

# function to add new candidate
def add_candidate(full_name, email, phone_number):
    with open(CSV_FILE1, 'a',newline='' ) as csvfile1:
        fieldnames = ['full_name', 'email', 'phone_number']
        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
        writer.writerow({'full_name': full_name, 'email': email, 'phone_number': phone_number})
    print(" candidate added successfully ")


# Function to list jobs
def list_jobs():
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        jobs = [row for row in reader]
    print("Job List:")
    for job in jobs:
        print(f"- {job['title']}: {job['description']}")

# Function to add a new job
def add_job(title, description):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        fieldnames = ['title', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'title': title, 'description': description})
    print("Job added successfully.")

# Main function
def main():
    while True:
        print("\n1. List Jobs")
        print("2. Add Job")
        print("3. list candidate")
        print("4. Add candidate")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_jobs()
        elif choice == '2':
            title = input("Enter job title: ")
            description = input("Enter job description: ")
            add_job(title, description)
        elif choice == '3':
            list_candidate()
        elif choice == '4':
            full_name = input("enter your full name: ")
            email = input("enter your email: ")
            phone_number = input("enter your phone number: ")
            add_candidate(full_name, email, phone_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()