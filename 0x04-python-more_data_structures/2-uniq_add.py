#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    total = 0
    for i in new:
        total += i
    return total
