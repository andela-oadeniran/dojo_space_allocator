#bin/python3*
class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self, name, room_type):
		self.name = name
		self.room_type = room_type


if '__name__' == '__main__':
    unittest.main()

