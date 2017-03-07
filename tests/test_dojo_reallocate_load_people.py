#!/usr/bin/env python

import os, sys
dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)



from dojo import Dojo
from models.fellow import Fellow
from models.staff import Staff
from models.living import LivingSpace
from models.office import Office

import unittest

class TestReallocatePerson(unittest.TestCase):
	"""Test suite for the reallocate person functionality"""
	def setUp(self):
		self.dojo = Dojo()

	def test_invalid_id_room(self):
		result = self.dojo.reallocate_person(2, 'Blue')
		self.assertEqual(result, 'Invalid Person Identifier or Room')

	def test_not_reallocate_to_present_room(self):
		self.dojo.create_room('office', ['Orion'])
		self.dojo.add_person('ladi', 'adeniran', 'fellow')
		result = self.dojo.reallocate_person(1, 'ORION')
		self.assertEqual(result, 'You cannot reallocate person to current room')
    
	def test_reallocate_fellow_staff_with_office(self):
		self.dojo.create_room('office', ['Naples'])
		self.dojo.add_person('brian','houston', 'fellow')
		self.dojo.add_person('ben', 'ayade', 'staff')
		fellow = self.dojo.app_session['person'][1]
		staff = self.dojo.app_session['person'][2]
		self.assertEqual(fellow.office, 'NAPLES')
		self.assertEqual(staff.office, 'NAPLES')
		self.dojo.create_room('office', ['Vienna'])
		self.dojo.reallocate_person(1, 'Vienna')
		self.dojo.reallocate_person(2, 'Vienna')
		self.assertEqual(fellow.office, 'VIENNA')
		self.assertEqual(staff.office, 'VIENNA')

	def test_reallocate_fellow_staff_with_no_office(self):
		self.dojo.add_person('ladi', 'adeniran', 'fellow')
		self.dojo.add_person('bayo', 'emmanuel', 'staff')
		fellow = self.dojo.app_session['person'][1]
		staff = self.dojo.app_session['person'][2]
		self.dojo.create_room('office', ['Blue'])
		self.assertFalse(fellow.office)
		self.assertFalse(staff.office)
		self.dojo.reallocate_person(1, 'Blue')
		self.dojo.reallocate_person(2, 'Blue')
		self.assertEqual(fellow.office, 'BLUE')
		self.assertEqual(staff.office, 'BLUE')

	def tearDown(self):
		del self.dojo


class TestLoadPeople(unittest.TestCase):
	'''Test suite for the load people from text file function'''

	def setUp(self):
		self.dojo = Dojo()

	def  test_load_file_exists_in_the_right_folder(self):
		 pass



















