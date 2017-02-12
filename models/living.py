from room import Room

class LivingSpace(Room):
	"""docstring for Living"""
	def __init__(self, room_name):
		super(LivingSpace, self).__init__(room_type='living', room_name=room_name)
		self.maxoccupant = 4
		# length not more than 4
		# can only have fellows

