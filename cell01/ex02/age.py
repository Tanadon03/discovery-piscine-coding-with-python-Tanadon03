import sys

a = 23
b = 42
my_age = str(a + b) + "\n"

sys.stdout.buffer.write(my_age.encode())
