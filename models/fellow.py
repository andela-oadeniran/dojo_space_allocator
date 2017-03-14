#!/usr/bin/env python

from person import Person


class Fellow(Person):
    """The Fellow class inherits from the Person Class"""

    def __init__(self, fname, lname, wants_accommodation):
        super(Fellow, self).__init__(fname=fname, lname=lname, role='fellow')
        self.wants_accommodation = wants_accommodation
        self.living_space = None

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)
