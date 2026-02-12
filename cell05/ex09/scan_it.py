#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
    sys.stdout.buffer.write(b"none\n")
else:
    params = len(sys.argv) - 1
    sys.stdout.buffer.write(f"{params}\n".encode())
