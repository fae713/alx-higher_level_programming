#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0 
    
    try:
        for Xelements in range(x):
            print(my_list[Xelements], end="")
            count += 1
    except IndexError:
        pass
    
    print()
    
    return count
