import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "./udp_socket_file"

client_address = "./udp_client_socket_file"

if os.path.exists(client_address):
    os.unlink(client_address)

message = "Message to send to the server"

sock.bind(client_address)

try:
    sent_count = 0
    while sent_count < 10:
        print(f"sending {message}")
        sent = sock.sendto(
            (message + f" sent count: {sent_count}").encode(), server_address
        )

        print("waiting to receive from server")

        data, _ = sock.recvfrom(4096)

        print(f"received {data.decode()}")

        sent_count += 1


finally:
    print("closing socket")
    sock.close()
