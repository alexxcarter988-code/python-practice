# Simple File Reader
# Author: Alex Carter

filename = "example.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    print("File contents:")
    print(content)

except FileNotFoundError:
    print("The file was not found.")

except PermissionError:
    print("Permission denied.")
