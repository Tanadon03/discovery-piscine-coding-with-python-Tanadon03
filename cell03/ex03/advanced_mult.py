#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    sys.stdout.buffer.write(b"none\n")
    sys.exit()

i = 0
while i <= 10:
    print(f"Table de {i}:", end="")
    
    j = 0
    while j <= 10:
        mul = i * j
        print(f" {mul}", end="")
        j += 1
    print()
    
    i += 1
