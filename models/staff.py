from person import Person

class Staff(Person):
	"""docstring for Staff"""
	def __init__(self, fname, lname):
		super(Staff, self).__init__(fname=fname, lname=lname, role='staff')


