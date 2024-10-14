import json
import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

config = json.load(open("config.json"))

server_address = config["socket_path"]

if os.path.exists(server_address):
    os.unlink(server_address)

print(f"Starting up on {server_address}")

dir = os.path.dirname(server_address)

if not os.path.exists(dir):
    os.mkdir(dir, mode=0o700)

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}")

        while True:
            data = connection.recv(64)

            data_str = data.decode("utf-8")

            print(f"Received data: {data}")

            if data:
                response = f"Processing {data_str}"
                connection.sendall(response.encode())
            else:
                print(f"no data from {client_address}")
                break
    finally:
        print("Closing current connection")
        connection.close()
