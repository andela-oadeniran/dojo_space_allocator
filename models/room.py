#!/usr/bin/env python


class Room(object):
    """docstring for Room: The class creates room objects for
    fellows and staff of Andela at The Dojo"""

    def __init__(self, room_type, name):
        self.name = name.upper()
        self.room_type = room_type
        self.occupants = []

    def __repr__(self):
        return '{}'.format(self.name.upper())


class Office(Room):
    """docstring for Office"""

    def __init__(self, name):
        super(Office, self).__init__(room_type='office', name=name)
        self.max_size = 6


class LivingSpace(Room):
    '''Class inherits from room class
    it has a maximum size of four(4) fellows'''

    def __init__(self, name):
        super(LivingSpace, self).__init__(room_type='living', name=name)
        self.max_size = 4
