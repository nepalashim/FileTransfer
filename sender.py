import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9090))

file_name = "CH10.pdf"
file_size = os.path.getsize(file_name)

# Sending file name and file size separately
client.send(file_name.encode())
client.recv(1024)  # Receiving acknowledgment from the receiver
client.send(str(file_size).encode())
client.recv(1024)  # Receiving acknowledgment from the receiver

# Send file data
with open(file_name, "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.sendall(data)

client.send("Image received".encode())

client.close()
