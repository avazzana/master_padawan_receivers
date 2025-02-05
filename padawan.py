import socket
import json
import sys
import time
import datetime
from LogFile import Log

MAX_WAIT_TIME = 1 * 60 # 5 minutes timeout

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f"server_{timestamp}.txt"
        self.log = Log(self.filename)
        sys.stdout = self.log
        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.host, self.port)
         # Wait for a message from the server
        message = self.receive_message() # Receive the message (up to 1024 bytes)

        # Print the received message
        print(f"Anakin: received message from server: {message}")



    def close(self):
        self.server.close()
        print("Obi-Wan: Server closed!")
        self.log.close()




    def send_message(self, message_type, step_id, body=None):
        print(f"Sending {message_type} command to client {self.client_id}")
        message = json.dumps({'type': message_type, 'step_id' : step_id, "body": body}).encode()
        self.clientSocket.sendall(message)
    

    def receive_message(self):
        data = self.client.recv(1024)
        if not data:
            print("Anakin: no data received")
        message = json.loads(data.decode())
        print(f"Message from {self.host}: {message}")

        if 'step_id' not in message:
            print("Invalid message:", message)

        if message['step_id'] == 1:
            print(message)
                
        elif message['step_id'] == 2:
            print(message)

        elif message['step_id'] == 4:
            print(message) 
             

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 12345
    client = Client(host, port)
    client.connect()

