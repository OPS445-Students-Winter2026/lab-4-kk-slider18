#!/usr/bin/env python3
# Author ID: kmitchell34

def is_digits(sobj):
    # place code here - loop through each character in sobj
    s1 = str(sobj)
    no_dig = 0
    for char in s1:
        if char not in '0123456789':
            no_dig += 1
        else:
            continue
    if no_dig > 0:
        return False
    else:
        return True
        
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')