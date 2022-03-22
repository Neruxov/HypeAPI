class NoArgumentsException(Exception):
    def __init__(self, message="Required arguments not presented"):
        self.message = message

    def __str__(self):
        return self.message


class APIException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
