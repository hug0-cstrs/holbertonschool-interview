#!/usr/bin/python3
# This is a shebang line which tells the system this script is a Python3
# script.


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    count = 0
    i = 2
    while i <= n:
        if n % i == 0:
            count += i
            n = n / i
            i = i - 1
        i = i + 1
    return count
