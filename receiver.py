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

received_message = client.recv(1024).decode()
print("Received Multimedia Sharing:", received_message)


client.close()
server.close()

