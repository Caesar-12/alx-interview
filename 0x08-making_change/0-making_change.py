#!/usr/bin/python3
"""Contains makeChange"""


def makeChange(coins, total):
    """Returns the least number of coins
    needed to make the total
    """
    if total <= 0:
        return 0
    if total in coins:
        return 1

    chk = 0
    while chk == 0:
        for ind in range(len(coins) - 1):
            if coins[ind] < coins[ind + 1]:
                hold = coins[ind]
                hold2 = coins[ind + 1]
                coins[ind] = hold2
                coins[ind + 1] = hold
                chk += 1
        if chk > 0:
            chk = 0
        else:
            chk = 2

    count = 0
    tots = total
    for coin in coins:
        while tots >= coin:
            tots -= coin
            count += 1

    if count == 0 or tots != 0:
        return -1
    else:
        return count
