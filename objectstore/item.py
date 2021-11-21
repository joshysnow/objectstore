#!/usr/bin/env python3

class Item:
    """
    An interesting item, worlds your oyster!
    """
    
    MIN_NAME_LENGTH = 5

    def __init__(self, id:int, name:str, colours:int):
        self.__id = id
        self.name = name
        self.colours = colours

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.MIN_NAME_LENGTH:
            raise ValueError(f'Name needs to be at least ${self.MIN_NAME_LENGTH} characters long')
        
        self.__name = value

    @property
    def colours(self):
        return self.__colours

    @colours.setter
    def colours(self, value):
        if value < 0:
            raise ValueError(f'Colours must be equal to or greater than 0')

        self.__colours = value
