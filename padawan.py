import socket
import json
import sys
import time
import datetime
from LogFile import Log

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.id = "Anakin"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f"padawan_{timestamp}.txt"
        self.log = Log(self.filename)
        sys.stdout = self.log
        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.receive_message() 
        self.close()




    def close(self):
        self.server.close()
        print("Anakin: Server closed!")
        self.log.close()




    def send_message(self, message_type, step_id, body):
        print(f"Anakin: Sending {message_type} command to client {self.client_id}")
        message = json.dumps({'type': message_type, 'sender_id' : self.id, 'step_id' : step_id, "body": body}).encode()
        self.clientSocket.sendall(message)
    

    def receive_message(self):
        data = self.client.recv(1024)
        if not data:
            print("Anakin: no data received")
        message = json.loads(data.decode())
        print(f"Anakin: received message from {self.host}: {message}")
        

        if 'step_id' not in message:
            print("Invalid message:", message)

        if message['step_id'] == 1:
            print(message)
                
        elif message['step_id'] == 2:
            print(message)

        elif message['step_id'] == 4:
            print(message) 
             

if __name__ == "__main__":
    host = '192.168.0.153'  # Use your Wi-Fi IPv4 address
    port = 5000
    client = Client(host, port)
    client.connect()

