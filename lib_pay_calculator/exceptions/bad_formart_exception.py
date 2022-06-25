

class BadFormatError(Exception):
    """
    Exception throwable when one function receives a parameter with a bad format
    """
    def __init__(self, message = "illegal arguments errors", format_expected = "") -> None:       
        super().__init__(f"Exception: {message}\nformat expected:\n{format_expected}")