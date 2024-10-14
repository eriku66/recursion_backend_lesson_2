import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "./udp_socket_file"

if os.path.exists(server_address):
    os.unlink(server_address)

print(f"Starting up on {server_address}")

sock.bind(server_address)

while True:
    print("\nwaiting to receive message")

    data, client_addresss = sock.recvfrom(4096)

    print(f"received {len(data)} bytes from {client_addresss}")

    print(data.decode())

    if data:
        sent = sock.sendto(
            f"Received {data.decode()} at the server".encode(), client_addresss
        )
        print(f"sent {len(data)} bytes back to {client_addresss}")
