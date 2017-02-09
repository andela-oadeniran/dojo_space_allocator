from models.room import Room

class Dojo():
	"""The class serves as the project's controller"""
	def __init__(self):
		pass

	#methods that interact with class Room
	def create_room(self, room_type, room_names):
		new_room = Room()
		new_room.create_room(room_type, room_names)
		# for room in room_names:
		# 	if room_type.lower() == "living":
		# 		new_room = Living(name=room)
		# 	elif room_type.lower() == "office":
		# 		new_room = Office(name=room)
