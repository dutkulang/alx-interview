#!/usr/bin/python3
""" Working on pascal's triangle
"""

def pascal_triangle(n):
    """
    returns a nested list of integers representing the
    pascal's triangle
    """
    final_list = []
    if type(n) is not int or n <=0:
        return final_list
    else:
        for i in range(n):
            line = []
            for q in range(i+1):
                if q == 0 or q == i:
                    line.append(1)
                elif i > 0 and q > 0:
                    line.append(final_list[i -1][q-1] + final_list[i-1][q])
            final_list.append(line)
        return final_list