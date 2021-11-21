#!/usr/bin/env python3
from objectstore.observer import Observer

class Subject:
    def __init__(self):
        self.__subscribers = []

    def subscribe(self, observer: Observer):
        if observer and isinstance(observer, Observer):
            self.__subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        if observer and isinstance(observer, Observer):
            self.__subscribers.remove(observer)

    def _notify_all(self):
        for subscriber in self.__subscribers:
            subscriber.notify(self)
