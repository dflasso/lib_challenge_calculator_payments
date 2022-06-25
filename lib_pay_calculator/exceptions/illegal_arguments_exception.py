
class IllegalArgumentsError(Exception):
    """
    Exception throwable when one function receives a parameter that broken business rules.
    """


    def __init__(self, message = "illegal arguments errors", sub_errors = []) -> None:
        
        summary_sub_errors = ""

        self.message = message
        self.sub_errors = sub_errors

        if isinstance(sub_errors, list):
            for sub_err in sub_errors:
                    summary_sub_errors += str(sub_err)
        
        
        super().__init__(f"Exception: {message}\nSub errors:\n{summary_sub_errors}")