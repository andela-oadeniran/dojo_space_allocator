from person import Person


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, fname, lname, wants_accommodation):
        super(Staff, self).__init__(fname=fname, lname=lname, role='staff')
        self.wants_accommodation = None

    def __repr__(self):
        return '{0} {1}'.format(self.fname, self.lname)

    