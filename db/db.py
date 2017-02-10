import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)

from office import Office
from living import LivingSpace
from fellow import Fellow
from staff import Staff

office_arr = []
living_arr = []
room_state = {'office':office_arr, 'living':living_arr}

fellow_arr = []
staff_arr = []
person_state = {'fellow':fellow_arr, 'staff' : staff_arr}


class Db(object):

	def __init__(self):
		room_state = {'office': []}

	# Methods interacting with Room, Office and LivingSpace classes
	# Office methods
	def create_office(self, office_name):
		self.office_name = Office(office_name)

		room_state['office'].append(self.office_name.room_name)
		print("An office called "+ room_state['office'][0]+(" has been successfully created"))
		print (room_state)

	def create_living_space(self, living_name):
		self.living_name = LivingSpace(living_name)
		room_state['living'].append(self.living_name.room_name)
		print(room_state)


