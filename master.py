import socket
import json
import sys
import time
import datetime
from LogFile import Log

MAX_WAIT_TIME = 5 * 60 # 5 minutes timeout

class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f"server_{timestamp}.txt"
        self.log = Log(self.filename)
        sys.stdout = self.log
        self.clientAddress = None
        self.clientSocket = None
        self.client_id = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.settimeout(MAX_WAIT_TIME)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Obi-Wan: Server started on {self.host}:{self.port}")
        self.wait_for_client_connection()

    def wait_for_client_connection(self):
        while self.clientAddress is None:
                try:
                    self.clientSocket, self.clientAddress = self.server.accept()
                    message = "Obi-Wan here. Congratulations Anakin, you are connected. But this doesn't mean you're on the jedi council"
                    step_id = 1
                    type = "start_rx_command"
                    self.send_message(type, step_id, message)
                    self.close()
                except socket.timeout:
                    print("Obi-Wan: Timeout waiting for Padawan Client")
                    return
    
    def send_start_rx_command(self):
        message = "Obi-Wan here. Anakin, stop being salty and start receiving signals"
        step_id = 2
        type = "start_rx_command"
        self.send_message(type, step_id, message)
        self.close()

    def lazy_boss_things(self):
        print("not yet implemented")

    def send_stop_rx_command(self):
        print("not yet implemented")

    def listen_for_stop_rx_confirmation(self):
        print("not yet implemented")

    def close(self, exc_type, exc_value, traceback):
        self.server.close()
        print("Obi-Wan: Server closed!")
        self.log.close()


    
    
    def send_message(self, message_type, step_id, body=None):
        print(f"Sending {message_type} command to client {self.client_id}")
        message = json.dumps({'type': message_type, 'step_id' : step_id, "body": body}).encode()
        self.clientSocket.sendall(message)

    def receive_message(self):
        data = self.clientSocket.recv(1024)
        if not data:
            print("Obi-Wan: no data received")
        message = json.loads(data.decode())
        print(f"Message from {self.clientAddress}: {message}")

        if 'step_id' not in message:
            print("Invalid message:", message)

        if message['step_id'] == 3:
            print(message)
            
        elif message['step_id'] == 5:
            print(message)
                




if __name__ == "__main__":
    host = '10.69.108.4'  # Use your Wi-Fi IPv4 address
    port = 5000
    server = Server(host, port)
    server.start_server()
