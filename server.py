import socket

class Server:
    def __init__(self, host="0.0.0.0", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)  # Listen for 1 connection

    def start(self):
        print("Server is waiting for a connection...")
        conn, addr = self.server_socket.accept()
        print(f"Connected by {addr}")

        for _ in range(10):
            message = conn.recv(1024).decode()
            print(f"Client says: {message}")
            conn.sendall(("hi client. It's your server here. Round " + str(_) + "\n").encode())

        print("Closing connection.")
        conn.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = Server()
    server.start()