# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class BadResponseFromAPI(Error):
    """Raised when there is a bad response from the API"""
    pass








