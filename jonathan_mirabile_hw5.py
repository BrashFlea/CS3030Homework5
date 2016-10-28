#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys
import re
def atm():
    """
    This program takes a PIN from the user and validates it.
    If the wrong pin is used more than 3 times, the program will exit with error code 1
    Args:
        PIN
    Returns:
        Nothing
    """


def validate_pin(arg):
    """
    Validate that user pin is 4 digits
    Args:
        PIN
    Returns:
        True/False
    """
    return bool(re.fullmatch("\d{4}", arg))


def getInput(arg):
    """
    Take user input and determine if valid. Prints to screen.
    Args:
        PIN
    Returns:
        Nothing
    """
arg = input('Enter your PIN: ')
pin = "1234"
tries = 3
while(tries > 0):
    if validate_pin(arg) ==  True:
        if arg == pin:
            print("Your PIN is correct")
            exit(0)
        else:              
            print("Your PIN is incorrect")
            tries = tries - 1
            arg = input('Enter your PIN: ')

    if validate_pin(arg) == False:
        print("Invalid PIN format. Correct format is: <9876>")
        tries = tries - 1
        arg = input('Enter your PIN: ')
        
if tries == 0:
    print("Your bank card is blocked")
    exit(1)



# Main function
def main():
    return


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

