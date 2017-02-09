#!bin/python

import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)

from person import Person

import unittest

class TestAddPerson(unittest.TestCase):
	"""The tests cases for the """
	def test_add_person_fellow(self):
		new_person = Person("ladi", "FELLOW")
		self.assertTrue(new_person)
		self.assertEqual(new_person.name, "ladi")
		self.assertEqual(new_person.type, "FELLOW")
	def test_add_person_staff(self):
		new_person = Person("newman", "STAFF")
		self.assertTrue(new_person)
		self.assertEqual(new_person.name, "newman")
		self.assertEqual(new_person.type, "STAFF")
	def test_person_can_either_be_fellow_staff(self):
		new_person = Person("zeus", "god")
		self.assertFalse(new_person)



if '__name__' == '__main__':
    unittest.main()

