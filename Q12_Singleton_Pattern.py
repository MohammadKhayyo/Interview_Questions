"""12. Suppose you're building a logging library for a web application that needs to keep
track of all requests and responses. You want to use the Singleton pattern to ensure
that there's only one instance of the logger class throughout the application."""


class SingletonMeta(type):
    """
    A Singleton metaclass that creates and manages a single instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """
    Logger class that implements the Singleton pattern.
    """

    def __init__(self):
        self.logs = []

    def log_request(self, request):
        # Implement logging logic for requests
        self.logs.append(f"Request: {request}")

    def log_response(self, response):
        # Implement logging logic for responses
        self.logs.append(f"Response: {response}")

    def show_logs(self):
        return self.logs


if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()

    logger1.log_request("GET /home")
    logger2.log_response("200 OK")

    # Both logger1 and logger2 are the same instance
    print(logger1 is logger2)  # True
    print(logger1.show_logs())  # Shows logs from both logger1 and logger2
