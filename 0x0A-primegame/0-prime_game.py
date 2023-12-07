#!/usr/bin/python3

"""Contains isWinner function that determines the winner of most round
    in a game where each users picks a prime number from a range of
    individual number in a list of number
"""


def is_prime(num):
    """Determines if a number is a prime number"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of most round"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = 0
        n_range = [x for x in range(1, n + 1)]

        for i in n_range:
            if is_prime(i):
                prime_count += 1

        if prime_count == 0:
            ben_wins += 1
        elif prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
