# Simple Hostname Lookup
# Author: Alex Carter

import socket


hostname = input("Enter a hostname: ")

try:
    ip_address = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("Unable to resolve hostname.")
