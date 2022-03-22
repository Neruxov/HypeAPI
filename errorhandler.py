class NoArguments(Exception):
    def __init__(self, message="Required arguments not presented"):
        self.message = message

    def __str__(self):
        return self.message
