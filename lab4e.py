#!/usr/bin/env python3

# Author ID: 174646232

def is_digits(sobj):
    false_c = 0
    for char in sobj:
        if char in '0123456789':
            true_c = 1
        else:
            false_c = 1
    if false_c == 1:
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