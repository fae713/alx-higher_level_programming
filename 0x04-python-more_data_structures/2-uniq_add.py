#!/usr/bin/bash
def uniq_add(my_list=[]):
    uniq_add = set()
    sum = 0

    for num in my_list:
        if num not in uniq_add:
            sum += num
            uniq_add.add(num)

    return sum
