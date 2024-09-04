## Student Name: Jayesh Naidu 
## Student ID: 1233830964 
## Date: 31-08-24

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9020))  # Connect to the server
    print("Connected to the server.")

    while True:
        # Send a message to the server
        message = input("Client: ")
        client_socket.sendall(message.encode())
        if message.lower() == 'bye':
            print("Client disconnected.")
            break

        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")
        if response.lower() == 'bye':
            print("Server disconnected.")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()