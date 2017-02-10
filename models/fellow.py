from person import Person

class Fellow(Person):
	"""docstring for Fellow"""
	def __init__(self, fname,lname, person_type, want_accom='N'):
		super(Fellow, self).__init__(fname=fname, lname=lname , person_type='fellow')
		self.want_accom = want_accom

