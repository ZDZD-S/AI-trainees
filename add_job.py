from data_handler import DataHandler
from utils.constants import JOB_FILE_NAME
# Functionality to save job details to a CSV file using the DataHandler class.
class job:
    job_counter = 0
    # Define column names for the CSV file as a class attribute
    headers = ['id', 'title', 'department', 'job_type', 'description', 'requirements', 'salary_range', 'current_status']
    # Initializes a new job posting with various details and a unique ID.
    def __init__(self, title, department, job_type, description, requirements, salary_range, current_status):
        job.job_counter += 1
        self.id = job.job_counter
        self.title = title
        self.department = department
        self.job_type = job_type
        self.description = description
        self.requirements = requirements
        self.salary_range = salary_range
        self.current_status = current_status
    # Saves the job posting details to a CSV file using DataHandler.
    def save(self):
        job_data = {
            'id': self.id,
            'title': self.title,
            'department': self.department,
            'job_type': self.job_type,
            'description': self.description,
            'requirements': self.requirements,
            'salary_range': self.salary_range,
            'current_status': self.current_status
        }
        
        # Initialize DataHandler with file name and headers
        data_handler = DataHandler(JOB_FILE_NAME, job.headers)
        data_handler.save_data(job_data)