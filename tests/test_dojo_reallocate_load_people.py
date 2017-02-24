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
	def test_reallocate_person_successfully(self):
		dojo = Dojo()
		new_staff = dojo.add_person('James', 'Peter','staff')
		self.assertEqual(new_staff.office, None)
		new_room = dojo.create_room('office', ['Ake'])
		dojo.reallocate_person(1, 'Ake')
		self.assertEqual(new_staff.office, 'Ake')
class TestLoadPeople(unittest.TestCase):
	"""Test suite for the load people functionnality"""
	def test_load_people(self):
		pass
