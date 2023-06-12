#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible_list = []
    for num in my_list:
        divisible_list.append(num % 2 == 0)
    return divisible_list
