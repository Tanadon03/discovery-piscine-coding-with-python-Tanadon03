#!/usr/bin/env python

try:
    a = input("Give me a number: ").strip()
    num = float(a)
    if num%1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass
