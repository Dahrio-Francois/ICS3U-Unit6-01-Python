#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# This program finds the average of 10 random numbers

import random


def main():

    random_numbers = []

    loop_counter = 0
    average = 0
    # input
    print("Here are the 10 numbers:")

    while loop_counter < 10:
        random_variable = random.randint(0, 100)
        random_numbers.append(random_variable)
        average = average + random_variable

        loop_counter = loop_counter + 1
    print("")
    print(random_numbers)
    average = average / 10
    print("The average of these 10 numbers is {}".format(average))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
