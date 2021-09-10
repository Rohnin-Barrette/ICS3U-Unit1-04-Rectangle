#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# This is the "Hello, World!" Program, with proper style


def main():
    length = 5
    width = 3
    print("calculate the area and the perimiter of the following")
    print("area = length * width ")
    print(
        "area of  {}cm * {}cm = {}cm^2  ".format(length, width, length * width)
    )
    print("\ncalculate the perimiter of the following")
    print("perimiter = (length + width) *2")
    print(
        "perimiter of  {}cm + {}cm = {}cm   ".format(
            length, width, (length + width) * 2
        )
    )


if __name__ == "__main__":
    main()
