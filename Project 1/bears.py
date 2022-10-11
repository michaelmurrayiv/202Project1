"""
Michael Murray
4/7/22

This code takes an integer, n, and determines if that integer can be transformed to 42 while following a specific set
of rules. The code checks all possibilities if an integer fits multiple rules.
"""


def bears(n):
    if n == 42:  # If the goal of 42 bears has been reached, returns True
        return True
    elif n < 42:  # If the goal is unreachable, returns False
        return False
    else:
        # calculates the last digit in n and the second to last digit, in order to use rule 2
        last_digit = n % 10
        second_to_last_digit = (n % 100) // 10

        # return statement checks if a rule works and if the bears call is true: this means it recursively tests all
        # the rules n can follow
        return (n % 2 == 0 and bears(n / 2)) or \
               (n % 3 == 0 or n % 4 == 0) and last_digit * second_to_last_digit and (
                           n - last_digit * second_to_last_digit) \
               or (n % 5 == 0 and bears(n - 42))
