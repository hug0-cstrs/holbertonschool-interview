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
    # Initialize total_operations to keep track of the total num of operations
    total_operations = 0
    # Initialize current_sum to 1 as we start with one 'H' character
    copy_value = 0
    # Initialize copy_value to keep track of the last copied value
    current_sum = 1

    # Loop until current_sum is less than n
    while current_sum < n:

        # If current_sum is a multiple of n
        if n % current_sum == 0:
            # Update copy_value with the value of current_sum
            copy_value = current_sum
            # Double the current_sum as we paste the copied value
            current_sum *= 2
            # Increment total_operations as copy operation is performed
            total_operations += 1
        else:
            # Add the copy_value to current_sum as we paste the copied value
            current_sum += copy_value
        # Increment total_operations as paste operation is performed
        total_operations += 1

    return total_operations  # Return the total number of operations
