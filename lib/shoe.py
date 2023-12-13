#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="Old"):
        self.brand = brand 
        self._size = size 
        self.condition = condition

    # @property
    # def size(self):
    #     return self._size 
    
    # @size.getter 
    # def size(self):
    #     return self._size 
    
    # @size.setter
    # def size(self, val):
    #     if(isinstance(val, int)):
    #         self._size = val 
    #     else: 
    #         print("size must be an integer")

    def get_size(self):
        return self._size 
    def set_size(self, val):
        if(isinstance(val, int)):
            self._size = val 
        else: 
            print("size must be an integer")
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"