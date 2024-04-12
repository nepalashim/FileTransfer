# import os 
# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("localhost",9090))

# file=open("image.png","rb")
# file_size = os.path.getsize("image.png")

# client.send("received_image.png".encode())
# client.send(str(file_size).encode())

# data=file.read()
# client.sendall(data)
# client.send(b"<END>")

# file.close()
# client.close()
# import os
# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("localhost", 9090))

# file_name = "image.png"
# file_size = os.path.getsize(file_name)

# # Send file name
# client.send(file_name.encode())

# # Send file size
# client.send(str(file_size).encode())

# # Send file data
# with open(file_name, "rb") as file:
#     while True:
#         data = file.read(1024)
#         if not data:
#             break
#         client.sendall(data)

# client.close()
import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9090))

file_name = "image.png"
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

client.close()
