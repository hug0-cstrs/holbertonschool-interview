#!/usr/bin/python3

"""
Minimum operations module
Using 'prime factorization' approach
Number of prime factors --> numbers of operators
== operations to get n's 'H'
"""


def minOperations(n):
    '''
    Method to compute the fewest number of operations
    to reach exactly 'n' times 'H' characters in the file
    Text editor can only do 'Paste' and 'Copy all' operations
    '''
    if not isinstance(n, int):
        return 0
    if n == 1:
        return 0
    ops = 0
    # 2 smallest prime number
    i = 2
    while i <= n:
        if n % i == 0:
            # bam => find a prime factor
            ops += i
            n /= i
            # n can't still be divisible by 'i', don't miss that
            # e.g. 24 /2 = 12 still divisible by 2 so i-=1 i+=1 we check again
            i -= 1
        i += 1
    return int(ops)
