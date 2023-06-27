#!/usr/bin/python3
"""defines class square """
class Square:
    def __init__ (self, length):
        self.length = length

    def getArea (self):
        return self.length ** 2
