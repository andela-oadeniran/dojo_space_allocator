from person import Person

class Fellow(Person):
	"""docstring for Fellow"""
	def __init__(self, fname, lname, wants_accommodation= 'n'):
		super(Fellow, self).__init__(fname=fname, lname=lname, role='fellow')
		self.wants_accommodation = wants_accommodation



