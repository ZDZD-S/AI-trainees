from enum import Enum, auto
from datetime import datetime

COURSES_CSV_PATH = 'courses.csv'

CONFIG_PATH = 'C:/Users/AbdulmajidAltowejri/Desktop/Projects/courses_management/config.ini'

DATE = datetime.now().strftime("%Y-%m-%d")

class MenuChoices(Enum):
    ADD_COURSE = auto()
    DROP_COURSE = auto()
    LIST_COURSES = auto()
    EXIT = auto()
