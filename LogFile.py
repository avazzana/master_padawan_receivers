import sys
import datetime

class Log:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.original_stdout = sys.stdout  # Save the original stdout

    def write(self, message):
        self.original_stdout.write(message)  # Print to console
        self.file.write(message)  # Write to file

    def flush(self):
        self.original_stdout.flush()
        self.file.flush()

    def close(self):
        sys.stdout = self.original_stdout  # Restore original stdout
        self.file.close()