#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    found = False
    
    for param in sys.argv[1:]:

        if not param.endswith("ism"):
            result = param + "ism\n"
            sys.stdout.buffer.write(result.encode())
            found = True
else:
    sys.stdout.buffer.write(b"none\n")
