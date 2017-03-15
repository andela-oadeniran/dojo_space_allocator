class Person(object):
    """Class helps create a Person object
    that can be subsequetly allocated a room.
    """

    def __init__(self, fname, lname, role, wants_accommodation=None):
        self.fname = fname.title()
        self.lname = lname.title()
        self.role = role
        self.id = None
        self.office = None
        self.wants_accommodation = wants_accommodation
        self.pname = '{0} {1} ({2})'.format(fname.title(),
                                            lname.title(), role.upper())

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, fname, lname):
        super(Staff, self).__init__(fname=fname, lname=lname, role='staff')
        self.wants_accommodation = None

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)


class Fellow(Person):
    """The Fellow class inherits from the Person Class"""

    def __init__(self, fname, lname, wants_accommodation=None):
        super(Fellow, self).__init__(fname=fname, lname=lname, role='fellow')
        self.wants_accommodation = wants_accommodation
        self.living_space = None

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)
