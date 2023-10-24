#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for Xelements in range(0, x):
        if isinstance(my_list[Xelements], int):
            try:
                print("{:d}".format(my_list[Xelements]), end='')
                num += 1
            except IndexError:
                pass
    print()
    return num
