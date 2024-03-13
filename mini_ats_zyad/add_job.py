import csv
import os

# Define a class named 'job' to represent a job
class job:
    job_counter = 0
    headers = ['id', 'title', 'description']

    # Constructor method to initialize a new job instance
    def __init__(self, title, description):
        job.job_counter += 1
        self.id = job.job_counter
        self.title = title
        self.description = description

    # Method to save job details to a CSV file
    def save(self):
        file_exists = os.path.isfile('jobs.csv')  # Check if 'jobs.csv' already exists

        with open('jobs.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)

            if not file_exists:
                writer.writeheader()  # Write column titles to the CSV if the file does not exist
            writer.writerow({'id': self.id, 'title': self.title, 'description': self.description})