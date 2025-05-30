#!/usr/bin/env python3

# String 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(ff_str):
    return ff_str[0:5]

def last_seven(l7_str):
    return l7_str[-7:]

def middle_number(mn):
    return str(mn)[1:3]

def first_three_last_three(f3, l3):
    str_f3l3 = f3[0:3] + l3[-3:]
    return str_f3l3

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))