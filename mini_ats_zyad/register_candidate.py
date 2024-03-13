import csv
import os

# Define a class 'candidate' to represent a job candidate
class candidate:
    Candidate_counter = 0
    headers = ['id', 'name', 'phone number', 'email']  # Define column names for the CSV file

    # Constructor method for initializing a new candidate instance
    def __init__(self, name, phonenumber, email):
        candidate.Candidate_counter += 1
        self.id = candidate.Candidate_counter
        self.name = name 
        self.email = email 
        self.phonenumber = phonenumber  

    # Method to save candidate details to a CSV file
    def save(self):
        file_exists = os.path.isfile('candidate.csv')  # Check if 'candidate.csv' exists already

        with open('candidate.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers) 

            if not file_exists:
                writer.writeheader()
            # Write the candidate's details as a new row in the CSV file
            writer.writerow({'id': self.id, 'name': self.name, 'phone number': self.phonenumber, 'email': self.email})