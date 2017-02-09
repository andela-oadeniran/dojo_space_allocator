class Person(object):
	"""docstring for Person: The class helps to create instances of the
	person object at Andela's Dojo"""
	def __init__(self, name, type):
		self.name = name


class Fellow(object):
	"""docstring for Fellow"""
	def __init__(self, arg):
		super(Fellow, self).__init__()
		self.arg = arg

class Staff(object):
	"""docstring for Staff"""
	def __init__(self, arg):
		super(Staff, self).__init__()
		self.arg = arg
