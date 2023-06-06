#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper_char = chr(ord(char) & 223)
        print('{}'.format(upper_char), end='')
    print()
