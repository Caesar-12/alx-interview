#!/usr/bin/python3
"""Contains minOperations function"""


def minOperations(n: int) -> int:
    """Calculates and return the fewest number of operation needed"""

    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible operations

        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]
