from person import Person

class Fellow(Person):
	"""docstring for Fellow"""
	def __init__(self, fellow_name, wants_accommodation='n'):
		super(Fellow, self).__init__(person_name=fellow_name, person_type='fellow')
		self.wants_accommodation = wants_accommodation



