from person import Person

class Fellow(Person):
	"""docstring for Fellow"""
	def __init__(self, fname, lname):
		super(Fellow, self).__init__(fname=fname, lname=lname, role='fellow')



