import socket
import json
import sys
import time
import datetime
from LogFile import Log

MAX_WAIT_TIME = 1 * 60 # 5 minutes timeout

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
        self.id = 'Obi Wan'

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.settimeout(MAX_WAIT_TIME)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Obi-Wan: Server started on {self.host}:{self.port}")
        self.send_connection_confirmation()
    
    def send_connection_confirmation(self):
        self.send_message("connection_confirmation", 1, "Hi Anakin, it's Obi Wan. \nYou're connected but you're still not part of the jedi council")
    
    def wait_for_client_ack(self):
        self.receive_message()

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
        self.receive_message()

    def close(self):
        self.server.close()
        print("Obi-Wan: Server closed!")
        self.log.close()


    
    
    def send_message(self, message_type, step_id, body):
        print(f"Sending {message_type} command to client {self.client_id}")
        message = json.dumps({'type': message_type, 'sender_id' : self.id, 'step_id' : step_id, "body": body}).encode()
        self.server.sendall(message)

    def receive_message(self):
        data = self.server.recv(1024)
        if not data:
            print("Obi-Wan: no data received")
        message = json.loads(data.decode())
        print(f"Message from {self.clientAddress}: {message}")

        if 'step_id' not in message:
            print("Invalid message:", message)
        elif message['step_id'] == 1:
            self.send_start_rx_command()
        elif message['step_id'] == 3:
            self.send_stop_rx_command()
        elif message['step_id'] == 5:
            self.close()
                




if __name__ == "__main__":
    host = '0.0.0.0'  # Use your Wi-Fi IPv4 address
    port = 5000
    server = Server(host, port)
    server.start_server()
