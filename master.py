import socket
import json
import sys
import time
import datetime
from LogFile import Log
import random
import keyboard

MAX_WAIT_TIME = 20
MIN_RX_POWER = 40
MAX_RX_POWER = 50

class Server:

    def __init__(self, host, port, save):
        self.host = host
        self.port = port
        self.save = save
        self.clientAddress = None
        self.clientSocket = None
        self.client_id = None
        self.id = 'Obi Wan'
        self.max = random.randint(1, 5)
        if self.save:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.filename = f"ServerLogs/server_{timestamp}.txt"
            self.log = Log(self.filename)
            sys.stdout = self.log

    def start_server_0(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.settimeout(MAX_WAIT_TIME)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Obi-Wan: Server started on {self.host}:{self.port}")
        self.wait_for_client_connection_0()

    def wait_for_client_connection_0(self):
        while self.clientAddress is None:
            try:
                if keyboard.is_pressed("x"):  # Check if 'x' is pressed
                    return
                self.clientSocket, self.clientAddress = self.server.accept()
                self.send_connection_confirmation_1()
            except socket.timeout:
                print("Obi-Wan: Timeout waiting for Padawan Client")
                return
    
    def send_connection_confirmation_1(self):
        message = "Obi-Wan here. Congratulations Anakin, you are connected. But this doesn't mean you're on the jedi council"
        step_id = 1
        type = "connection_confirmation"
        self.send_message(type, step_id, message)
        self.wait_for_client_ack_2()

    def wait_for_client_ack_2(self):
        message = self.receive_message()
        if 'step_id' not in message:
            print("Invalid message:", message)
        elif message['step_id'] == 2:
            self.client_id = message['sender_id']
            self.send_start_rx_command_3()
        else:
            print("wrong message id. expected 2, got ", message['step_id'])

    def send_start_rx_command_3(self):
        step_id = 2
        type = "start_rx_command"
        rx_power = random.randint(MIN_RX_POWER, MAX_RX_POWER)
        body = "Obi-Wan here. Anakin, I need you to start receiving signals at " + rx_power + " dBw" 
        print(f"Sending {type} command to client {self.clientAddress}")
        message = json.dumps({'type': type, 'sender_id' : self.id, 'step_id' : step_id, 'rx_power' : rx_power, "body": body}).encode()
        self.clientSocket.sendall(message)
        self.close_server_connection_8()

    def collect_and_boss_4(self):
        print("not yet implemented")
        self.close_server_connection_8()

    def send_stop_rx_command_5(self):
        print("not yet implemented")

    def listen_for_stop_rx_confirmation_6(self):
        self.receive_message()

    def confirm_close_7(self):
        print("not implemented yet")

    def close_server_connection_8(self):
        self.server.close()
        print("Obi-Wan: Server closed!")
        if self.save:
            self.log.close()


    
    
    def send_message(self, message_type, step_id, body):
        message = json.dumps({'type': message_type, 'sender_id' : self.id, 'step_id' : step_id, "body": body}).encode()
        print(f"{self.id} here, sending to {self.client_id} the following message\n{message}")
        self.clientSocket.sendall(message)

    def receive_message(self):
        data = self.server.recv(1024)
        if not data:
            print("Obi-Wan: no data received")
        message = json.loads(data.decode())
        print(f"Message from {self.clientAddress}: {message}")
        return message
                




if __name__ == "__main__":
    host = '0.0.0.0'  # Use your Wi-Fi IPv4 address
    port = 5000
    server = Server(host, port, True)
    server.start_server_0()
