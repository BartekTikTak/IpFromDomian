import socket
import time

domain = input(">")

try:
    ip = socket.gethostbyname(domain)
    print(f"IP serwera dla domeny {domain} to: {ip}")
except socket.gaierror:
    print("Nie można odnaleźć adresu IP dla podanej domeny.")
time.sleep(120)
