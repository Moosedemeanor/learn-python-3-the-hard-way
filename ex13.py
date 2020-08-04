# import argv from the sys module
from sys import argv
# read the wyss section for how to run this
script, first, second = argv
third=input("Please type a third input: ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
