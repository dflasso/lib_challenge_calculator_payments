
class ErrorModel:
    """
    DTO standard for to launch errors
    """

    message = ""
    code = "0000"
    field = ""
    obj = ""

    def __init__(self, message  , code = "0000", field = "", obj  = "") -> None:
        self.message = message
        self.code = code
        self.field = field
        self.obj = obj


    def __str__(self) -> str:
        if self.obj != "" and self.field != "":
            return f"ERROR [{self.code}] : {self.message} (Object: {self.obj}, Field: {self.field}) \n"    

        return f"ERROR [{self.code}] : {self.message} \n"