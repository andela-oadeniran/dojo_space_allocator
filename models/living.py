from room import Room

class LivingSpace(Room):
	"""docstring for Living"""
	def __init__(self, name):
		super(LivingSpace, self).__init__(purpose='living_space', name=name)
		self.max_size = 4
		# length not more than 4
		# can only have fellows

