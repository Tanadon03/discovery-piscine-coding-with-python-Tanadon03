#!/usr/bin/env python
import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        result = list(range(start, end + 1))
        sys.stdout.buffer.write(f"{result}\n".encode())
        
    except ValueError:
        sys.stdout.buffer.write(b"none\n")
else:
    sys.stdout.buffer.write(b"none\n")
