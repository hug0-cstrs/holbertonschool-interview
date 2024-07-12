#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:  # if total is 0 or less, 0 coins are needed
        return 0
    coins.sort(reverse=True)  # sort coins in descending order
    num_coins = 0  # number of coins needed
    for coin in coins:  # iterate through coins
        if total <= 0:  # if total is 0 or less, 0 coins are needed
            break  # exit loop
        num_coins += total // coin  # add number of coins needed to num_coins
        total = total % coin  # update total
    if total != 0:  # if total is not 0, total cannot be met
        return -1  # return -1
    return num_coins  # return number of coins needed
