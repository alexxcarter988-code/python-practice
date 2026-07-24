# python-practice
Small Python scripts and exercises created while learning Python for security automation and everyday tasks.


# Python Practice

A collection of small Python exercises and scripts created while learning Python.

I'm using this repository to practice Python fundamentals and explore how Python can be useful for automation, networking, and cybersecurity.

---

## Topics Covered

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- File handling
- Exception handling
- Regular expressions
- Basic networking concepts
- Simple automation

---

## 🐍 Python Basics

### Hello World

```python
print("Hello, World!")
```

### Variables

```python
name = "Alex"
age = 37

print("Name:", name)
print("Age:", age)
```

### Simple Calculation

```python
a = 10
b = 20

result = a + b

print("Result:", result)
```

---

##  Loops

### For Loop

```python
for number in range(1, 6):
    print(number)
```

### While Loop

```python
counter = 1

while counter <= 5:
    print(counter)
    counter += 1
```

---

## Conditional Statements

```python
age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

##Lists

```python
tools = [
    "Linux",
    "Wireshark",
    "Nmap",
    "Python"
]

for tool in tools:
    print(tool)
```

---

## Functions

```python
def greet(name):
    print("Hello,", name)


greet("Alex")
```

---

## File Handling

### Reading a File

```python
with open("example.txt", "r") as file:
    content = file.read()

print(content)
```

### Writing to a File

```python
with open("output.txt", "w") as file:
    file.write("Python practice file")
```

---

## Regular Expressions

A simple example of finding email addresses in text.

```python
import re

text = "Contact us at example@example.com"

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
)

print(emails)
```

---

##  Basic Networking

### Check a Hostname

```python
import socket

hostname = socket.gethostname()

print("Hostname:", hostname)
```

### Resolve a Domain

```python
import socket

domain = "example.com"

ip_address = socket.gethostbyname(domain)

print("Domain:", domain)
print("IP Address:", ip_address)
```

---

## Simple IP Address Validation

```python
import ipaddress

ip = input("Enter an IP address: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP address")
except ValueError:
    print("Invalid IP address")
```

---

##  Simple Automation

Example of listing files in the current directory.

```python
import os

files = os.listdir(".")

for file in files:
    print(file)
```

---

## Cybersecurity Learning

I'm currently exploring how Python can be used for:

- Automation
- Log analysis
- File processing
- Network programming
- Data parsing
- Security tool development
- Repetitive task automation

---

## Current Learning Goals

- Improve Python fundamentals
- Learn object-oriented programming
- Practice working with APIs
- Explore automation
- Learn Python for cybersecurity
- Build small practical projects

---

##  Notes

This repository contains small exercises and experiments created while learning Python.

Some scripts may be simple or incomplete as this is primarily a learning repository.

Learning by building, breaking, and improving.
