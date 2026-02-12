#!/usr/bin/env python
import sys

def greetings(name="noble stranger"):
    if isinstance(name, str):
        res = f"Hello, {name}.\n"
    else:
        res = "Error! It was not a name.\n"
    
    sys.stdout.buffer.write(res.encode())

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
