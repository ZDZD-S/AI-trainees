from data_handler import DataHandler
from utils.constants import CANDIDATE_FILE_NAME
# Functionality to save candidate details to a CSV file using the DataHandler class.
class candidate:
    candidate_counter = 0
    # Define column names for the CSV file as a class attribute
    headers = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'linkedin_profile', 'education', 'experience', 'skills']
    # Initializes a new candidate posting with various details and a unique ID.
    def __init__(self, first_name, last_name, email, phone_number, address, linkedin_profile, education, experience, skills):
        candidate.candidate_counter += 1
        self.id = candidate.candidate_counter
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.linkedin_profile = linkedin_profile
        self.education = education
        self.experience = experience
        self.skills = skills
    # Saves the candidate details to a CSV file using DataHandler.
    def save(self):
        # Data to be saved
        candidate_data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address,
            'linkedin_profile': self.linkedin_profile,
            'education': self.education,
            'experience': self.experience,
            'skills': self.skills
        }
        
        # Initialize DataHandler with file name and headers
        data_handler = DataHandler(CANDIDATE_FILE_NAME, candidate.headers)
        data_handler.save_data(candidate_data)