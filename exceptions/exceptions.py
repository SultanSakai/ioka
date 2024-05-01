# exceptions.py


class ioka_api_error(Exception):
    def __init__(self, message):
        self.message = message


class connection_error(Exception):
    def __init__(self, message):
        self.message = message
