#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: October 2019
# This program finds if a rectangle is a square


def main():
    # this function finds if a rectangle is a square

    # input
    length = int(input("Give me the length (cm): "))
    width = int(input("Give me the width (cm): "))

    # process and output
    print("your rectangle is")
    if length == width:
        print("a square")
    elif length != width:
        print("not a square")
    else:
        print("Error, it is not a rectangle")


if __name__ == "__main__":
    main()
