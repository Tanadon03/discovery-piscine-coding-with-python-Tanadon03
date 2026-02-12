#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    sys.stdout.buffer.write(sys.argv[1].encode()+b"\n")
else:
    sys.stdout.buffer.write(b"none\n")
