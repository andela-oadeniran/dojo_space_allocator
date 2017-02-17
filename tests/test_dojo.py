#!/usr/bin/env python

import os, sys
dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)

from dojo import Dojo
from models.fellow import Fellow
from models.staff import Staff

import unittest

class TestCreateRoom(unittest.TestCase):
    """Write Docstring here """
    def test_created_office_successfully(self):
    	dojo = Dojo()
    	initial_room_count = len(dojo.all_rooms)
    	blue_office = dojo.create_room("office", ['Blue'])
    	self.assertEqual(blue_office.name, 'Blue')
    	self.assertEqual(blue_office.purpose, 'office')
    	self.assertEqual(blue_office.max_size, 6)
    	new_room_count = len(dojo.all_rooms)
    	room_count_diff = new_room_count - initial_room_count
    	self.assertEqual(room_count_diff, 1)



    def test_created_living_space_successfully(self):
    	dojo = Dojo()
    	initial_room_count = len(dojo.all_rooms)
    	orange_living_space = dojo.create_room('living', ['Orange'])
    	self.assertEqual(orange_living_space.name, 'Orange')
    	self.assertEqual(orange_living_space.purpose, 'living')
    	self.assertEqual(orange_living_space.max_size, 4)
    	new_room_count = len(dojo.all_rooms)
    	room_count_diff =  new_room_count - initial_room_count
    	self.assertEqual(room_count_diff, 1)
    def test_created_multi_offices_or_living_spaces(self):
    	dojo = Dojo()
    	initial_room_count = len(dojo.all_rooms)
    	multi_offices = dojo.create_room('office', ['Orion', 'Dev', 'fly'])
    	new_room_count = len(dojo.all_rooms)
    	room_count_diff = new_room_count - initial_room_count
    	self.assertEqual(room_count_diff, 3)
    def test_room_uniqueness(self):
    	dojo = Dojo()
    	initial_room_count = len(dojo.all_rooms)
    	amigo_office = dojo.create_room('office', ['amigo','amigo'])
    	new_room_count = len(dojo.all_rooms)
    	room_count_diff = new_room_count - initial_room_count
    	self.assertEqual(room_count_diff, 1)

    def test_create_room_is_only_for_offices_living_spaces(self):
    	dojo = Dojo()
    	other_pupose_room = dojo.create_room('kitchen', ['Puerto'])
    	self.assertIsNone(other_pupose_room)




class TestAddPerson(unittest.TestCase):
    """The test suite for the  Dojo Method add_person"""
    def test_fellow_staff_added_successfully(self):
    	dojo = Dojo()
    	new_fellow = dojo.add_person('Ladi', 'Adeniran', 'fellow', 'y')
    	new_staff = dojo.add_person('Usman', 'Ibrahim', 'staff')
    	self.assertTrue(new_fellow)
    	self.assertTrue(new_staff)

    	self.assertEqual(new_fellow.fname, 'Ladi')
    	self.assertEqual(new_staff.fname, 'Usman')
    	self.assertEqual(new_fellow.role, 'fellow')

    	self.assertIsInstance(new_fellow, Fellow)
    	self.assertIsInstance(new_staff, Staff)

    	self.assertTrue(new_fellow.wants_accommodation)

    	self.assertEqual(new_fellow.wants_accommodation, 'y')


#     	# self.assertFalse(new_staff.living_space.name)




if '__name__' == '__main__':
    unittest.main()
