#!/usr/bin/env python

from room import Room


class Office(Room):
    """docstring for Office"""

    def __init__(self, name):
        super(Office, self).__init__(room_type='office', name=name)
        self.max_size = 6
