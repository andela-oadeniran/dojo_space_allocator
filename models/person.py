
class Person(object):
	"""docstring for Person: The class helps to create instances of the
	person object at Andela's Dojo"""
	def __init__(self, fname,lname, role):
		self.fname = fname
		self.lname = lname
		self.role = role
	def __repr__(self):
	    return '{0} {1}'.format(self.fname, self.lname)

