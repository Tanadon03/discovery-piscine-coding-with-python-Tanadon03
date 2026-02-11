#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
    sys.stdout.buffer.write(b"none\n")
else:
    reversed_params = sys.argv[1:][::-1]
    for param in reversed_params:
        sys.stdout.buffer.write(param.encode() + b"\n")
