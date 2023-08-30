#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title 
        self._page_count = page_count

    # @property 
    # def page_count(self):
    #     return self._page_count 
    
    # @page_count.getter
    # def page_count(self):
    #     return self._page_count 
    
    # @page_count.setter
    # def page_count(self, val):
    #     if isinstance(val, int):
    #         self._page_count = val 
    #     else: 
    #         print("page_count must be an integer")

    def set_page_count(self, val):
            if isinstance(val, int):
                self._page_count = val 
            else: 
                print("page_count must be an integer")
    def get_page_count(self):
         return self._page_count
    page_count = property(get_page_count, set_page_count)
    
    def turn_page(self):
         print( "Flipping the page...wow, you read fast!")
        