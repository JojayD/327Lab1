#!/usr/bin/env python3
import socket
import sys
import os

INTRA_PORT = 5004
INTER_PORT = 5003


def start_listener():
    sock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR ,1)
    sock.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEPORT ,1)

    try:
        sock.bind(("0.0.0.0" ,INTRA_PORT))
        print(f"Node listening on port {INTRA_PORT}")

        while True:
            try:
                data ,addr = sock.recvfrom(1024)
                message = data.decode()
                print(f"Received: {message} from {addr[0]}")
            except KeyboardInterrupt:
                print("\nShutting down...")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()
if __name__ == "__main__":
    start_listener()