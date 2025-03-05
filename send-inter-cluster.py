import socket

PORT = 5004  # Port used for inter-cluster communication
CLUSTER_A_MASTER_IP = "192.168.100.2"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello, Cluster B!"
sock.sendto(message.encode(), (CLUSTER_A_MASTER_IP, PORT))
print(f"Sent inter-cluster message: {message}")