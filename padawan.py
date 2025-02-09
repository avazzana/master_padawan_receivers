import socket
import json
import sys
import time
import datetime
from LogFile import Log
import random

class Client:

    def __init__(self, host, port, save):
        self.host = host
        self.port = port
        self.save = save
        self.id = "Anakin"
        self.client = None
        self.step = 0
        self.max = random.randint(1, 5)
        if self.save:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.filename = f"padawan_{timestamp}.txt"
            self.log = Log(self.filename)
            sys.stdout = self.log


    def connect_0(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.wait_for_server_confirmation_1()
 
    def wait_for_server_confirmation_1(self):
        message = self.receive_message()
        if 'step_id' not in message:
            print("Invalid message:", message)
        elif message['step_id'] == 1:
            self.sendACK_2()
        else:
            print("wrong message id. expected 1, got ", message['step_id'])



    def sendACK_2(self):
        type = "ready_for_rx_command"
        id = 2
        body = "Hello Obi Wan! I am ready for my command!"
        self.send_message(type, id, body)
        self.wait_for_start_rx_command_3()
    
    def wait_for_start_rx_command_3(self):
        com = self.receive_message()
        if com['step_id'] != 3:
            print(f"invalid command, id should be 3 but was {com['step_id']}")
        else:
            rx_power = com['rx_power']
            self.collect_and_confirm_4(rx_power)

    def collect_and_confirm_4(self, rx_power):
        print("4 not implemented yet")
        self.close_client_connection_8()

    def wait_for_stop_rx_command_5(self):
        print("5 not implemented yet")

    def stop_rx_and_repeat_6a(self):
        print("6a not implemented yet")

    def stop_rx_and_close_connection_6b(self):
         print("6b not implemented yet")

    def wait_for_close_confirmation_7(self):
         print("7 not implemented yet")
   
    def close_client_connection_8(self):
        self.client.close()
        print("Anakin: client connection closed!")
        if self.save:
            self.log.close()




    def send_message(self, message_type, step_id, body):
        print(f"Anakin: Sending {message_type} message to client {self.id}")
        message = json.dumps({'type': message_type, 'sender_id' : self.id, 'step_id' : step_id, "body": body}).encode()
        self.client.sendall(message)
    

    def receive_message(self):
        data = self.client.recv(1024)
        if not data:
            print("Anakin: no data received")
        message = json.loads(data.decode())
        print(f"Anakin: received message from {self.host}: {message}")
        return message
             

if __name__ == "__main__":
    host_home = '192.168.0.153'  # Use your Wi-Fi IPv4 address
    host_school = '10.69.108.4'
    host = host_home
    port = 5000
    client = Client(host, port, False)
    client.connect_0()

