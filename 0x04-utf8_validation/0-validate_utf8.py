#!/usr/bin/python3
"""Contains the function validUTF8"""


def validUTF8(data):
    """Determines if a set of data validates utf-8 encoding"""

    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if num >> 7 == 0b0:
                continue
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if num >> 6 == 0b10:
                num_bytes -= 1
            else:
                return False

    if num_bytes == 0:
        return True
