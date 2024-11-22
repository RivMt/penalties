import socket
import asyncio

import config_loader as config
import logger
import audio
import facial
import window

MAX_EXIT_COUNT = 2

server_ip = config.get_host_address()
server_port = config.get_port()
server_addr_port = (server_ip, server_port)
buffer_size = config.get_buffer_size()

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind(server_addr_port)
udp_server_socket.setblocking(False)
udp_server_socket.settimeout(config.get_timeout())


# Scores
emotion_score = 0
speech_score = 0
physics_score = 0

# Listen Datagram incoming
async def main():
    global emotion_score, speech_score, physics_score
    logger.log(server_ip, "UDP Server Initialized")
    exit_count = 0
    while True:
        try:
            byte_addr_pair = udp_server_socket.recvfrom(buffer_size)
        except BlockingIOError:
            logger.log(server_ip, "Packet blocked")
            continue
        except TimeoutError:
            continue
        except KeyboardInterrupt:
            if exit_count < MAX_EXIT_COUNT:
                logger.log(server_ip, f"Press Ctrl+C {MAX_EXIT_COUNT - exit_count} times")
                exit_count += 1
                continue
            exit()
        packet_message = byte_addr_pair[0].decode("unicode_escape").encode('latin1').decode('utf-8').lower()
        packet_address = (byte_addr_pair[1][0])
        packet_port = byte_addr_pair[1][1]

        if "emotion" in packet_message:
            data = packet_message.split(" ")
            facial.append_history(data[1])
            facial.append_history(data[2])
            emotion_score = facial.calc_score()
            logger.log("Emotion", f"{emotion_score:2f} ({data[1]}/{data[2]})")
            if emotion_score > 15:
                await window.display()
            else:
                await window.minimize()
        elif "speech" in packet_message:
            data = packet_message.split(" ", maxsplit=2)
            speech_score = float(data[1])
            message = data[2]
            logger.log("Speech", f"{speech_score:.2f}: {message})")
        elif "physics" in packet_message:
            data = packet_message.split(" ", maxsplit=1)
            physics_score = float(data[1])
            logger.log("Physics", f"{physics_score:.2f}")
        else:
            logger.log(f"{packet_address}:{packet_port}", packet_message)

if __name__ == "__main__":
    main_loop = asyncio.get_event_loop()
    main_loop.run_until_complete(main())
    main_loop.close()