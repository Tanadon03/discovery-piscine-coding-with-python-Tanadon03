#!/usr/bin/env python

input1 = int(input("Enter the first number : \n"))
input2 = int(input("Enter the  second number : \n"))
mul = input1 * input2
print(input1, "x", input2, "=", mul)
if mul < 0:
    res = "The result is negative.\n"
elif mul > 0:
    res = "The result is positive.\n"
else:
    res = "The result is positive and negative.\n"
print(res)
