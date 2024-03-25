import csv
import os
from utils.errors import FILE_WRITE_ERROR

# Manages CSV file writing, including file creation and appending data with proper headers.
class DataHandler:
    # Initializes the handler with CSV file name and headers.
    def __init__(self, file_name, headers):
        self.file_name = file_name
        self.headers = headers
    # Saves data to CSV. Creates the file with headers if it doesn't exist.
    def save_data(self, data):
        try:
            file_exists = os.path.isfile(self.file_name)
            with open(self.file_name, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
        except Exception as e:
            print(f"{FILE_WRITE_ERROR} - {e}")