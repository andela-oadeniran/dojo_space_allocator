
class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self,purpose, name):
		self.name = name
		self.purpose = purpose
		self.occupants = []
		self.size = 0
		if self.occupants:
			self.size = len(self.occupants)


if '__name__' == '__main__':
    unittest.main()


