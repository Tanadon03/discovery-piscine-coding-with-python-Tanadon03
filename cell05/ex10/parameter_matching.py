#!/usr/bin/env python
import sys

if len(sys.argv) == 2:
    secret_word = sys.argv[1]
    
    user_guess = input("What was the parameter? ")
    
    if user_guess == secret_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
        
else:
    print("none")
