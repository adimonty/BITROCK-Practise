import os
from threading import Lock

class Logger:

    _instance = None
    _lock = Lock()

    def __init__(self):
        if not Logger._instance:
            print("Initializing the logger...")
            Logger._instance = self
            self.log_file = "application_log.txt"
        else:
            raise Exception("Cannot instantiate a second logger instance.")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = Logger()
        return cls._instance

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')
        print(f"Logged: {message}")

# Usage
logger = Logger.get_instance()

# Log some messages
logger.log("Application started.")
logger.log("User logged in.")
logger.log("Data processed.")

# Check the log file
with open(logger.log_file, 'r') as f:
    print("Log file contents:")
    print(f.read())
