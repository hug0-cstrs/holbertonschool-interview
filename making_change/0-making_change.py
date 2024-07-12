#!/usr/bin/python3
'''Making Change module'''


def makeChange(coins, total):
    """
    Function that given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total < 1:  # if total is 0 or less
        return 0
    change = 0  # number of coins
    coins.sort(reverse=True)  # sort coins in descending order
    for coin in coins:  # iterate through coins
        temp_change = int(total / coin)  # number of coins of particular value
        total -= (temp_change * coin)  # subtract the value of coins from total
        change += temp_change  # add the number of coins to change
        if total == 0:
            return change
    if total != 0:
        return -1
