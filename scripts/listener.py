#!/usr/bin/env python3
import socket

PORT = 5005

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))  # Listen on all interfaces
    print(f"[Listener] Listening on port {PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode().strip()
        print(f"[Received] from {addr}: {message}")

if __name__ == "__main__":
    main()
