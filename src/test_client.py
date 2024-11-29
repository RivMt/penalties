import socket

import config_loader as config

server_ip = config.get_target_address()
server_port = config.get_port()
server_addr_port = (server_ip, server_port)

try:
    while True:
        message = input()
        tag = "Debug"
        if " " in message:
            tag = message.split(" ", maxsplit=1)[0]
            message = message.split(" ", maxsplit=1)[1]
        bytes_to_send = str.encode(f"{tag} {message}")

        udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_client_socket.sendto(bytes_to_send, server_addr_port)
except KeyboardInterrupt:
    print()