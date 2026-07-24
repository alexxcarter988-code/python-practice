# Simple IP Address Validator
# Author: Alex Carter

import ipaddress


def validate_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True

    except ValueError:
        return False


ip = input("Enter an IP address: ")

if validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")
