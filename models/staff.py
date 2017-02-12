from person import Person

class Staff(Person):
	"""docstring for Staff"""
	def __init__(self, staff_name):
		super(Staff, self).__init__(person_name=staff_name,person_type='staff')


