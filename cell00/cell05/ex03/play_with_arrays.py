#!/usr/bin/env python

import sys
original = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = {x + 2 for x in original if x > 5}

sys.stdout.buffer.write(("Original array:" + str(original) + "\n").encode())
sys.stdout.buffer.write(("New array:" + str(new_array) + "\n").encode())
