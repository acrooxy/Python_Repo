import socket

# Define the server IP address
HOST = "127.0.0.1"

# Define the port number used for communication
PORT = 5000

print("Client is starting...")

try:
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    print("Connected to server.")

    # Send a request to the server
    message = "TIME"
    client_socket.send(message.encode())

    print("Request sent to server:", message)

    # Receive response from the server
    response = client_socket.recv(1024).decode()

    print("Response from server:")
    print(response)

    # Close the connection
    client_socket.close()

    print("Connection closed.")

except Exception as error:
    print("Connection failed.")
    print("Error:", error)