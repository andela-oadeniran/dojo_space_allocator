class Person(object):
    """Class helps create a Person object
    that can be subsequetly allocated a room.
    """

    def __init__(self, fname, lname, role):
        self.fname = fname
        self.lname = lname
        self.role = role
        # self.id = 0

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)
