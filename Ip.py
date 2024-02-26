import socket
import time

domain = input(">")

try:
    ip = socket.gethostbyname(domain)
    print(f"IP for  {domain} is: {ip}")
except socket.gaierror:
    print("Unable to find the IP address for the specified domain.")
time.sleep(120)
