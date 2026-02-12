# first_name = "Tanadon"
# last_name = "Aunyart"

# print(first_name + " " + last_name)

import sys

first_name = "Tanadon"
last_name = "Aunyart"

sys.stdout.buffer.write((first_name + " " + last_name + "\n").encode())
