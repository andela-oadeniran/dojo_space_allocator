#!/usr/bin/env python

import os, sys
dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)

from dojo import Dojo

import unittest

class TestCreateRoom(unittest.TestCase):
    """Write Docstring here """
    def test_created_office_successfully(self):
    	# dojo = Dojo()
    	# room = dojo.create_room(self, 'office', ['Blue'])
        initial_room_count = len(new_class.all_rooms)
        # blue_office = Room.create_room("Blue", "office")
        self.assertTrue(room)
        self.assertEqual(room.room_name, 'Blue')
        self.assertEqual(room.room_type, 'Office')

        # new_room_count = len(my_class_instance.all_rooms)
        # self.assertEqual(new_room_count - initial_room_count, 1)

    # def test_create_room_is_only_office_living:
    # 	new_class = Room()


class TestAddPerson(unittest.TestCase):
	"""The tests cases for the  Dojo Class"""
	def test_create_single_office(self):
		app_session_length = len(Dojo.app_session['room'])
		new_room = Dojo().create_room('office', ['Orange'])
		new_app_session_length = len(Dojo.app_session['room'])
		self.assertEqual(app_session_length+1, new_app_session_length)
		orange_room = next((x for x in Dojo.app_session['room'] if x.room_name == 'Orange'), None)
		self.assertTrue(orange_room.room_name, 'Blue')
		self.assertEqual(orange_room.room_type, 'office')

	def test_create_single_living(self):
		app_session_length = len(Dojo.app_session['room'])
		new_room = Dojo().create_room('living', ['Blue'])[0]
		new_app_session_length = len(Dojo.app_session['room'])

		# Test room is created
		self.assertEqual(new_room.room_name, 'Blue')
		self.assertEqual(new_room.room_type, 'living')
		self.assertEqual(app_session_length+1, new_app_session_length)

		# Test it is being saved
		blue_room = next((x for x in Dojo.app_session['room'] if x.room_name == 'Blue'), None)
		self.assertTrue(blue_room.room_name, 'Blue')
		self.assertEqual(blue_room.room_type, 'living')


	# def test_person_can_either_be_fellow_staff(self):
	# 	new_person = Person("Koya Adegboyega", "cod")
	# 	self.assertIsNone(new_person)



if '__name__' == '__main__':
    unittest.main()
