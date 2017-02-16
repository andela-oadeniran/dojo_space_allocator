class Person(object):
	"""docstring for Person: The class helps to create instances of the
	person object at Andela's Dojo"""
	def __init__(self, person_name, person_type):
		if person_type.lower() in ('fellow', 'staff'):
			self.person_name = person_name
			self.person_type = person_type
		else:
			print('Person must be a fellow or staff. Got {}'.format(person_type))
			return None


