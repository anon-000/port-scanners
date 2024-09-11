import sys
import socket
import threading
import time


usage = "Use it like : > python3 port_scan_L1.py TARGET_IP_ADDRESS START_PORT END_PORT"

begining_time = time.time()

print("Python Port Scanner ( Level 1 )")
print("=" * 40)

# Checing for invalid args
if (len(sys.argv) != 4):
    print(usage)
    sys.exit()

start_port = sys.argv[2]
end_port = sys.argv[3]

try:
    target = socket.gethostname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()


for port in range(start_port, end_port+1):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(2)
    connection_response = soc.connect_ex((target, port))
    if (not connection_response):
        print(f"Port {port} is Open")
    soc.close()


def scan_port():
    print("scainn")


ending_time = time.time()

print(f"Time Taken : ", ending_time - begining_time)
