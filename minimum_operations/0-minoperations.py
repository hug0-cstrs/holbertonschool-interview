#!/usr/bin/python3
"""Module which contains minoperations function"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
        to result in exactly n H characters in the file

        Args:
            n: repetitions of H

        Returns:
            number of operations (Copy & Paste) to reach n Hs
    """
    # Initialize the result and index variables
    result = 0
    index = 2

    # If n is less than 2, return 0 as no operations are needed
    if n < 2:
        return 0

    # Iterate from index 2 to n+1
    while (index < n + 1):

        # Check if the problem is evenly breakable
        while n % index == 0:

            # If so, add the number of smaller problems to the result
            result += index

            # Create the smaller problem needed to get to n
            n /= index

        # Increment the index to check the next number
        index += 1

    # Return the result of the operations
    return result
