#!/usr/bin/python3
"""Contains rorate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Rotates matrix 90 degree"""
    n = len(matrix)

    trans_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]

    rot_matrix = [list(reversed(row)) for row in trans_matrix]
    matrix[:] = rot_matrix[:]
