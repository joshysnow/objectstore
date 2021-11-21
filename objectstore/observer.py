#!/usr/bin/env python3

class Observer:
    """
    Objects that are interested in a subject should
    inherit from this class.
    """

    def notify(self, sender: object):
        pass
