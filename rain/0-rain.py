#!/usr/bin/python3
"""
module rain contains a function to calculate how much water
will be retained after it rains.
"""


def rain(walls):
    """Calculate how much water will be retained after it rains."""
    if not walls:  # if walls is empty
        return 0

    n = len(walls)  # number of walls
    left = [0] * n  # leftmost wall
    right = [0] * n  # rightmost wall

    left[0] = walls[0]  # first wall
    for i in range(1, n):  # from the second wall to the last
        left[i] = max(left[i - 1], walls[i])  # max of left and current wall

    right[n - 1] = walls[n - 1]  # last wall
    for i in range(n - 2, -1, -1):  # from the second last wall to the first
        right[i] = max(right[i + 1], walls[i])  # max of right and current wall

    water = 0  # water retained
    for i in range(n):  # for each wall
        # min of left and right - current wall
        water += min(left[i], right[i]) - walls[i]

    return water  # return water retained
