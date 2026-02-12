#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    num_params = len(sys.argv) - 1
    
    para = f"parameters: {num_params}\n"
    sys.stdout.buffer.write(para.encode())
    
    for param in sys.argv[1:]:
        length = len(param)
        line = f"{param}: {length}\n"
        sys.stdout.buffer.write(line.encode())
else:
    sys.stdout.buffer.write(b"none\n")
