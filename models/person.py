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
