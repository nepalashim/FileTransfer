# import socket
# import tqdm

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost",9090))
# server.listen()

# client, addr = server.accept()

# file_name = client.recv(1024).decode()
# print(file_name)
# file_size = client.recv(1024).decode()
# print(file_size)

# file=open(file_name, "wb")
# file_bytes = b""
# done = False

# progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

# while not done:
#     data = client.recv(1024)
#     if file_bytes[-5:] == b"<END>":
#         done = True
#     else:
#         file_bytes += data
#     progress.update(1024)

# file.write(file_bytes)

# file.close()
# client.close()
# server.close()

# import socket
# import tqdm

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost", 9090))
# server.listen()

# client, addr = server.accept()

# # Receive file size
# file_size = int(client.recv(1024).decode())
# print("File size:", file_size)

# # Receive file name
# file_name = client.recv(1024).decode()
# print("File name:", file_name)

# file = open(file_name, "wb")

# progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)

# while True:
#     data = client.recv(1024)
#     if not data:
#         break
#     file.write(data)
#     progress.update(len(data))

# file.close()
# client.close()
# server.close()



import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9090))
server.listen()

client, addr = server.accept()

# Receiving file name
file_name = client.recv(1024).decode()
print("File name:", file_name)
client.send(b"OK")  # Sending acknowledgment to the sender

# Receive file size
file_size = int(client.recv(1024).decode())
print("File size:", file_size)
client.send(b"OK")  # Sending acknowledgment to the sender

file = open(file_name, "wb")

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)

while True:
    data = client.recv(1024)
    if not data:
        break
    file.write(data)
    progress.update(len(data))

file.close()
client.close()
server.close()

