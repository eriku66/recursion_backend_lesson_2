import json
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

config = json.load(open("config.json"))

server_address = config["socket_path"]

print(f"connecting to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = b"Sending a message to the server side"
    sock.sendall(message)

    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(64))

            if data:
                print(f"Server response: {data}")
            else:
                break
    except TimeoutError:
        print("Socket timeout, ending listening for server messages")

finally:
    print("closing socket")
    sock.close()
