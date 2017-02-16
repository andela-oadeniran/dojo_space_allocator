#!/bin/python

import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)

from person import Person

import unittest

class TestAddPerson(unittest.TestCase):
	"""The tests cases for the """
	def test_add_person_fellow(self):
		person = Person("Ladi Adeniran", "FELLOW")
		self.assertTrue(person)
		self.assertEqual(person.person_name, "Ladi Adeniran")
		self.assertEqual(person.person_type, "FELLOW")

	def test_add_person_staff(self):
		person = Person("Newman Philip", "STAFF")
		self.assertTrue(person)
		self.assertEqual(person.person_name, "Newman Philip")
		self.assertEqual(person.person_type, "STAFF")

	# def test_person_can_either_be_fellow_staff(self):
	# 	new_person = Person("Koya Adegboyega", "cod")
	# 	self.assertIsNone(new_person)



if '__name__' == '__main__':
    unittest.main()

