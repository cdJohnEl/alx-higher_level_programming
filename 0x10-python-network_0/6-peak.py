#!/usr/bin/python3
"""Defines an algorithm that finds the peak."""

def find_peak(list_integers):
    if list_integers == []:
        return None
    
    list_len = len(list_integers)
    i = int(list_len/2)
    list = list_integers

    if i - 1 < 0 and i + 1 >= list_len:
        return list[i]
    elif i - 1 < 0:
        return list[i] if list[i] > list[i + 1] else list[i + 1]
    elif i + 1 >= list_len:
        return list[i] if list[i] > list[i - 1] else list[i -1]

    if list[i - 1] < list[i] > list[i + 1]:
        return list[i]

    if list[i + 1] > list[i - 1]:
        return find_peak(list[i:])
    return find_peak(list[:i])