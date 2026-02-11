#!/usr/bin/env python
import math

try:
    a = input("Give me a number: ").strip()
    num = float(a)
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    pass
