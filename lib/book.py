#!/usr/bin/env python3
import ipdb 
class Book:
    def __init__(self, title, page_count):
        # print("initializing...")
        self.title = title #attributes
        self.page_count = page_count 
        #below would not invoke are setter method
        #you would be able to pass in values other than ints
        #self._page_count = page_count
    
    #property: page_count
    #attribute: _page_count
    #create methods to override inherent get/set
    # def get_page_count(self):
    #     # print("getting....")
    #     return self._page_count 
    
    # def set_page_count(self, val):
    #     # print("setting...")
    #     if(isinstance(val, int)):
    #         self._page_count = val 
    #     else: 
    #         print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # #let class know you are override inherent get/set by making page_count a property
    # page_count = property(get_page_count, set_page_count)
    
    @property 
    def page_count(self):
        return self._page_count
    
    @page_count.getter 
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, val):
        if(isinstance(val, int)):
            self._page_count = val 
        else: 
            print("page_count must be an integer")


    
        
hp = Book("hp", 3)
pj = Book("pj", 100)
no = Book("no", 25)
# ipdb.set_trace()
