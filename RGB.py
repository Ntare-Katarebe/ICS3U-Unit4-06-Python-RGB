#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the RGB
#    with numbers inputted from the user


def main():
    # This function prints the RGB
    RGB1 = 0
    RGB2 = 0
    RGB3 = 0

    # process & output
    for RGB1 in range(0, 255 + 1):
        for RGB2 in range(0, 255 + 1):
            for RGB3 in range(0, 255 + 1):
                print("RGB {},{},{}".format(RGB1, RGB2, RGB3))


if __name__ == "__main__":
    main()
