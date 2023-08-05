#!/usr/bin/python3
"""Contains function canUunlockall"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked"""
    n = len(boxes)
    visited = set()
    stack = [0]
    # Start with the first box (boxes[0])

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            keys = boxes[current_box]
            stack.extend(keys)

    # If all boxes are visited (i.e., the length of 'visited'
    # set is equal to the number of boxes 'n'), return True
    return len(visited) == n
