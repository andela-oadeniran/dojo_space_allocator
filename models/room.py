
class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self,room_type, room_name):
		self.room_name = room_name
		self.room_type = room_type
		self.occupants = {}
		#get the total number of rooms from the database.
		# self.allrooms = 0


if '__name__' == '__main__':
    unittest.main()

