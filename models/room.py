#!/usr/bin/env python


class Room(object):
    """docstring for Room: The class creates room objects for
    fellows and staff of Andela at The Dojo"""

    def __init__(self, room_type, name):
        self.name = name.upper()
        self.purpose = room_type
        self.occupants = []

    def __repr__(self):
        return '{}'.format(self.name.upper())
