import socket

class Client:
    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))

        for _ in range(10):
            self.client_socket.sendall("hi server. It's the client here. Round " + _ + "\n".encode())
            message = self.client_socket.recv(1024).decode()
            print(f"Server says: {message}")

        print("Closing connection.")
        self.client_socket.close()

if __name__ == "__main__":
    client = Client()
    client.start()