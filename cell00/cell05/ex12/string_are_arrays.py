#!/usr/bin/env python
import sys

from matplotlib.pylab import char

if len(sys.argv) == 2:
    input_word = sys.argv[1]
    result = ""
    
    for z in input_word:
        if z == 'z':
            result += "z"
            
    if result:
        output = result + "\n"
        sys.stdout.buffer.write(output.encode())
    else:
        sys.stdout.buffer.write(b"none\n")
else:
    sys.stdout.buffer.write(b"none\n")
