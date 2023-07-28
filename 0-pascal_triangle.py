#!/usr/bin/python3

"""
Returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    degree= []
    pascal_tri = []

    for i in range(n):
        if (i + 1) == 1:
            pascal_tri.append([1])
        elif (i + 1) == 2:
            pascal_tri.append([1, 1])
        else:
            for co_eff in range(len(pascal_tri[i - 1])):
                if co_eff == 0:
                    degree.append(1)
                else:
                    degree.append((pascal_tri[i - 1][co_eff]) + (pascal_tri[i - 1][co_eff - 1]))
            degree.append(1)
            pascal_tri.append(degree)
            #print("degree = ", degree)
            degree = []
        #print("pascal_tri = ", pascal_tri)
    
    return pascal_tri
        


