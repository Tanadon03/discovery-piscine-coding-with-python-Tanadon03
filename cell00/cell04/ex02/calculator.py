#!/usr/bin/env python

a = int(input("Give me the first number: ").strip())
b = int(input("Give me the second number: ").strip())
print("Thank you!")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Division by zero is undefined.")
