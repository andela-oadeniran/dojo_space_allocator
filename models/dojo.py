
import os, sys
dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db'))

sys.path.append(dbdir)

from db.db import Db
db = Db()

class Dojo():
	"""The class serves as the project's controller"""
	def __init__(self):
		pass

	#methods that interact with Room, Office and LivingSpace classes
	def create_room(self, room_type, room_names):
		# parse this and make an instance of room for each case
		# check to see whether room type is valid
		valid = ['office', 'living']
		if (room_type.lower() == valid[0]):
			for room_name in room_names:
				# appropriate instance of the db class
				db.create_office(room_name)

		elif (room_type.lower()== valid[1]):
			for room_name in room_names:
				#appropriate instance of the db class
				db.create_living_space(room_name)
		else:
			raise ValueError('Not a valid room_type')

	#methods interacting with the Person, Fellow and Staff classes

