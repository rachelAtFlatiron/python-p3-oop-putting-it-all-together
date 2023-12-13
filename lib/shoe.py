#!/usr/bin/env python3
import ipdb 
class Shoe:
    def __init__(self, brand, size, condition=None):
        self.brand = brand 
        self.size = size 
        self.condition = condition

    @property 
    def size(self):
        return self._size 
    @size.getter
    def size(self):
        return self._size 
    @size.setter 
    def size(self, val):
        if(isinstance(val, int)):
            self._size = val 
        else: 
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

ipdb.set_trace()