import socket
from datetime import datetime

# Define the server IP address
HOST = "127.0.0.1"

# Define the port number used for communication
PORT = 5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming client connections
server_socket.listen(1)

print("Server is running...")
print("Waiting for a client connection...")

# Accept a connection from a client
connection, address = server_socket.accept()

print("Client connected from:", address)

# Receive data from the client
message = connection.recv(1024).decode()

print("Message received from client:", message)

# Check the client's request
if message == "TIME":
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = "Current server time is: " + current_time
else:
    response = "Unknown request."

# Send the response back to the client
connection.send(response.encode())

# Close the connection and socket
connection.close()
server_socket.close()

print("Server closed.")