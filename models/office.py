#!/usr/bin/env python

from room import Room


class Office(Room):
    """docstring for Office"""

    def __init__(self, name):
        super(Office, self).__init__(purpose='office', name=name)
        self.max_size = 6
