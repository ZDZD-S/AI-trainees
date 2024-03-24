class CourseNotFoundError(Exception):
    """Exception raised when a course is not found in the registry."""
    pass

class CourseAlreadyExistsError(Exception):
    """Exception raised when trying to add a course that already exists."""
    pass

