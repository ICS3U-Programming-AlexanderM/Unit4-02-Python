#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 6 2022
# This program asks the user to enter a number
# and then uses a loop to calculate and display the factorial
# of that number.

def main():
    # determine loop and factorial variables
    loop = 0
    factorial = 1

    # get the user input
    user_number_string = input("Enter your number: ")
    print("")

    # check inputs
    try:
        user_number = int(user_number_string)
    except Exception:
        print("Invalid input, must be an integer.")
        quit()

    # check if number is positive or 0
    if user_number < 0:
        print("Number must be equal or greater than 0")
        quit()

    # calculate the factorial of user number
    while True:
        loop = loop + 1
        factorial = factorial * loop
        print("Tracking {} times through loop.". format(loop))
        if loop >= user_number:
            break

    print("")
    print("The factorial of {} is {}."
          . format(user_number, factorial))


if __name__ == "__main__":
    main()
