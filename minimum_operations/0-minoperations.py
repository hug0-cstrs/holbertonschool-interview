#!/usr/bin/python3
"""Module which contains minoperations function"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    
    Args:
        n: repetitions of H

    Returns:
        number of operations (Copy & Paste) to reach n Hs
    """
    # This is a function that takes an integer n as input.

    if n <= 1:
        return 0
    # If n is less than or equal to 1, the function returns 0. This is because
    # no operations are needed to get 1 H character.

    count = 0
    # Initialize a counter to keep track of the number of operations.

    i = 2
    # Initialize a variable i to 2. This will be used to divide n.

    while i <= n:
        # Start a while loop that continues as long as i is less than or equal
        # to n.

        if n % i == 0:
            # If n is divisible by i,

            count += i
            # add i to the count. This is because we can get i H characters by
            # copying the existing H character and pasting it i-1 times.

            n = n / i
            # Divide n by i. This is because we have reduced the problem to
            # finding the minimum number of operations to get n/i H characters.

            i = i - 1
            # Decrement i by 1. This is to check if the new n is divisible by a
            # smaller number.

        i = i + 1
        # Increment i by 1. This is to check if n is divisible by the next
        # number.

    return count
    # Return the count. This is the minimum number of operations needed to get
    # n H characters.
