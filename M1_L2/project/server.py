## Student Name: Jayesh Naidu 
## Student ID: 1233830964 
## Date: 31-08-24

import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9020))  # Bind to localhost and port 9020
    server_socket.listen(1)  # Listen for incoming connections
    print("Server is listening on port 9020...")

    client_socket, addr = server_socket.accept()  # Accept a connection
    print(f"Connection from {addr} has been established.")

    while True:
        # Receive the message from the client
        message = client_socket.recv(1024).decode()
        if message.lower() == 'bye':
            print("Client disconnected.")
            break
        print(f"Client: {message}")

        # Respond to the client
        response = input("Server: ")
        client_socket.sendall(response.encode())
        if response.lower() == 'bye':
            print("Server disconnected.")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()