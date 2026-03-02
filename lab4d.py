#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(ffive):
    # Place code here - refer to function specifics in section below
    return ffive[0:5]


def last_seven(lseven):
    # Place code here - refer to function specifics in section below
    return lseven[-7:]

def middle_number(mnum):
    # Place code here - refer to function specifics in section below
    str_out = str(mnum)
    return str_out[1:3]

def first_three_last_three(fthree, lthree):
    # Place code here - refer to function specifics in section below
    substring = fthree[0:3] + lthree[-3:]
    return substring


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))