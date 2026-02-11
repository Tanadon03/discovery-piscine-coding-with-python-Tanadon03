#!/usr/bin/env python


try:
    number = int(input("Enter a number less than 25: ").strip())
    if number <= 25:
        i = number
        while i <= 25:
            print("Inside the loop, my variable is", i)
            i += 1
    else:
        print("Error")
        
except ValueError:
    print("Error: Please enter a valid number.")
