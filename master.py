import socket
import json

def server_program():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 5000       

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Accept one client for simplicity

    print("Server listening for connections...")
    conn, address = server_socket.accept()
    print(f"Connection from {address}")

    # Handshake using JSON
    data = json.loads(conn.recv(1024).decode())  # Receive JSON and decode
    if data.get("type") == "SYN":
        print("Received SYN, sending SYN-ACK")
        conn.send(json.dumps({"type": "SYN-ACK"}).encode())

        data = json.loads(conn.recv(1024).decode())
        if data.get("type") == "ACK":
            print("Received ACK, handshake complete!")

    # Example: Sending a JSON message
    message = {"message": "Hello, client!", "status": "success"}
    conn.send(json.dumps(message).encode())

    conn.close()

if __name__ == "__main__":
    server_program()