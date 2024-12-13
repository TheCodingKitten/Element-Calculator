#!/usr/bin/env python
# 
# Element Shell Configurations
# https://github.com/TheCodingKitten/Element-Calculator
# 

from Element_Calculator_CLI import Elements
from Element_Calculator_CLI import Symbols

numberInput = int(input("Enter Atomic Number of an element: ")) # User input to numberInput variable
if numberInput < 1 or numberInput > 118: # Checks if atomic number is greater than 118 and closes script
    print("Error: Invalid input. Input must be between 1 and 118.")
    exit()

#Variables
num2 = numberInput - 2 # Remainder after shell 1
num3 = num2 / 8 # Number of shells
num4 = num2 % 8 # Remaining electrons in outer most shell
num5 = str(num4) # String of num4

# Print info about element
print("Element Name: ", Elements[numberInput],"\n" "Element Symbol: ", Symbols[numberInput], "\n" "Shell Configuration: ")
if numberInput <= 2: # Full inner shell only
    print(numberInput)
else: 
    if num4 == 0: # Full inner, full middle(s), full outer shells
        print("2", int(num3)*"8 ")
    else: # Full inner, full middle(s), not full outer shells
        print("2", int(num3)*"8 ", end=num5)
