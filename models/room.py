
class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self,room_type, room_name):
		self.room_name = room_name
		self.room_type = room_type
		self.room_occupants = []

	def add_room_size(self):
		self.room_size = len(self.room_occupants)
		return self.room_size
		#get the total number of rooms from the database.
		# self.allrooms = 0


if '__name__' == '__main__':
    unittest.main()

new_room = Room('living', 'orange')
new_room.room_occupants.append('ladi adeniran')
print(new_room.room_occupants)
new_room.add_room_size()
print(new_room.room_size)

new_room.room_occupants.append('ladi adeniran')
print(new_room.room_occupants)

print(new_room.room_size)

