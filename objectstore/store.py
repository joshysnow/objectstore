#!/usr/bin/env python3
from objectstore.subject import Subject
from objectstore.item import Item

class Store:
    """
    A collection of Items. Glorious!
    """

    def __init__(self):
        self.__store = []

    @property
    def store(self):
        return self.__store

    def add_item(self, item:Item):
        if item and isinstance(item, Item):
            self.__store.append(item)
            self._notify_all()

    def remove_item(self, item:Item):
        if item and isinstance(item, Item):
            self.__store.remove(item)
            self._notify_all()
