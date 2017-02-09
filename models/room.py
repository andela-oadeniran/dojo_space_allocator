#bin/python3*
class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self):
		pass
	def create_room(self, room_type, room_names):
		types = ["office","living" ]
		#test to see whether it is a valid room type
		if (room_type.lower() in types):
			if(room_type.lower()=="office"):
				#make each an instance of the Office class for each room_name
				for room_name in room_names:
					room_name = Office(room_name)
					print (room_name.arg)
			else:
				for room_name in room_names:
					#make each room an instance of the Living class
					room_name = Living(room_name)
					print (room_name.arg)
		else:
			raise ValueError("Not a valid room_type")
			return None
class Office(Room):
	"""docstring for Office"""
	def __init__(self, arg):
		# super(Office, self).__init__()
		#get the number of people in the room from room
		#and define the maximum number of people that can be in  an office
		self.count = 0
		self.maxnumber = 6
		while self.count < self.maxnumber:
		    self.arg = arg
		    self.count+=1
		else:
			return "OYO"

class Living(Room):
	"""docstring for Living"""
	def __init__(self, arg):
		super(Living, self).__init__()
		self.arg = arg


if '__name__' == '__main__':
    unittest.main()

