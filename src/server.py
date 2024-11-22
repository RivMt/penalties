import socket
import asyncio
from qasync import QEventLoop, asyncSlot

import config_loader as config
import logger
import audio
import facial
import window
import constants


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
debug_score = 0

# Listen Datagram incoming
async def main():
    # Init
    global emotion_score, speech_score, physics_score, debug_score
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
            if exit_count < constants.MAX_EXIT_COUNT:
                logger.log(server_ip, f"Press Ctrl+C {constants.MAX_EXIT_COUNT - exit_count} times")
                exit_count += 1
                continue
            exit()
        packet_message = byte_addr_pair[0].decode("unicode_escape").encode('latin1').decode('utf-8').lower()
        packet_address = (byte_addr_pair[1][0])
        packet_port = byte_addr_pair[1][1]

        # Handle message
        if "emotion" in packet_message:
            data = packet_message.split(" ")
            facial.append_history(data[1])
            facial.append_history(data[2])
            emotion_score = facial.calc_score()
            logger.log("Emotion", f"{emotion_score:2f} ({data[1]}/{data[2]})")
        elif "speech" in packet_message:
            data = packet_message.split(" ", maxsplit=2)
            speech_score = float(data[1])
            message = data[2]
            logger.log("Speech", f"{speech_score:.2f}: {message})")
        elif "physics" in packet_message:
            data = packet_message.split(" ", maxsplit=1)
            physics_score = float(data[1])
            logger.log("Physics", f"{physics_score:.2f}")
        elif "debug" in packet_message:
            data = packet_message.split(" ", maxsplit=1)
            debug_score = float(data[1])
            logger.log("Debug", f"{data[1]}")
        else:
            logger.log(f"{packet_address}:{packet_port}", packet_message)

        # Trigger action
        general_score = emotion_score + speech_score + physics_score + debug_score
        # Emotion
        if emotion_score > 15:
            await window.display_smile()
        else:
            await window.minimize_smile()
        # General
        await window.set_gauge(int(general_score))
        if general_score >= 500:
            await window.display_gauge()
        else:
            await window.minimize_gauge()

if __name__ == "__main__":
    # Integrate Async loop
    loop = QEventLoop(window.app)
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    loop.run_forever()