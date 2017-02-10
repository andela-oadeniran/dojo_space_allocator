from person import Person

class Staff(Person):
	"""docstring for Staff"""
	def __init__(self, fname, lname,person_type='staff'):
		super(Staff, self).__init__(fname=fname, lname= lname,person_type=person_type)
