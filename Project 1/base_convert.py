"""
Michael Murray
4/7/22

Function that takes a positive integer and a base, b, and returns a string representing the integer in base b
"""


def convert(num, b):
    # end condition
    if num // b == 0:
        if num % b == 10:
            return 'A'
        elif num % b == 11:
            return 'B'
        elif num % b == 12:
            return 'C'
        elif num % b == 13:
            return 'D'
        elif num % b == 14:
            return 'E'
        elif num % b == 15:
            return 'F'
        else:
            return str(num)

    # following elif statements account for remainders between 10 and 15 using appropriate letters
    elif num % b == 10:
        return convert(num // b, b) + 'A'
    elif num % b == 11:
        return convert(num // b, b) + 'B'
    elif num % b == 12:
        return convert(num // b, b) + 'C'
    elif num % b == 13:
        return convert(num // b, b) + 'D'
    elif num % b == 14:
        return convert(num // b, b) + 'E'
    elif num % b == 15:
        return convert(num // b, b) + 'F'

    # If the remainders are less than 10, add them to the final string
    else:
        return convert(num // b, b) + str(num % b)
