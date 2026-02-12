#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
    sys.stdout.buffer.write(b"none\n")
else:
    num_params = len(sys.argv) - 1
    sys.stdout.buffer.write(f"{num_params}\n".encode())
