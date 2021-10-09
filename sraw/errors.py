# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class BadResponseFromAPI(Error):
    """Raised when there is a bad response from the API"""
    pass

class NoTitleProvided(Error):
    """Raised when there the song title is not given"""
    pass

class NoPokemonProvided(Error):
    """Raised when there the pokemon name is not given"""
    pass

class NoKeyProvided(Error):
    """Raised when there the API key is not given"""
    pass

class NoMessageProvided(Error):
    """Raised when there the message is not given in the chatbot command"""
    pass



