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






