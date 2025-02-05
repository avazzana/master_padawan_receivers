import socket
import json

def client_program():
    host = '127.0.0.1'  # Change this to the server's IP if needed
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Handshake using JSON
    print("Sending SYN")
    client_socket.send(json.dumps({"type": "SYN"}).encode())

    data = json.loads(client_socket.recv(1024).decode())
    if data.get("type") == "SYN-ACK":
        print("Received SYN-ACK, sending ACK")
        client_socket.send(json.dumps({"type": "ACK"}).encode())

    # Receive a JSON message from the server
    message = json.loads(client_socket.recv(1024).decode())
    print(f"Server says: {message}")

    client_socket.close()

if __name__ == "__main__":
    client_program()