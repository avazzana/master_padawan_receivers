import sys
import os
import datetime

class Log:
    def __init__(self, file_path):
        # Ensure directories exist
        dir_name = os.path.dirname(file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        self.file = open(file_path, 'w')
        self.original_stdout = sys.stdout  # Save the original stdout
        sys.stdout = self  # Redirect stdout to this log class

    def write(self, message):
        self.original_stdout.write(message)  # Print to console
        self.file.write(message)  # Write to file

    def flush(self):
        self.original_stdout.flush()
        self.file.flush()

    def close(self):
        sys.stdout = self.original_stdout  # Restore original stdout
        self.file.close()