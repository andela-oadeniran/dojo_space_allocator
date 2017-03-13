#!/usr/bin/env python

from room import Room


class LivingSpace(Room):
    '''Class inherits from room class
    it has a maximum size of four(4) fellows'''

    def __init__(self, name):
        super(LivingSpace, self).__init__(room_type='living', name=name)
        self.max_size = 4
