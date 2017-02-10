from room import Room


class Office(Room):
	"""docstring for Office"""
	def __init__(self, room_name):
		super(Office, self).__init__(room_type='office', room_name=room_name)
		self.maxoccupant = 6
		#length not more than 6
		#can have member staff and fellow

