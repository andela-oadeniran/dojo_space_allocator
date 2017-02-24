#!/usr/bin/env python

import os
import sys
import unittest
modelsdir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)
from person import Person
from fellow import Fellow
from staff import Staff


class TestPersonClass(unittest.TestCase):
    """The test for the Person Model, its attributes
    and mehods."""

    def test_created_person_successfully(self):
        new_person = Person(fname='Ladi', lname='Adeniran',
                            role='software developer')
        self.assertTrue(new_person)
        self.assertIsInstance(new_person, Person)
        self.assertEqual(new_person.fname, 'Ladi')
        self.assertEqual(new_person.lname, 'Adeniran')
        self.assertEqual(new_person.role, 'software developer')


class TestFellowClass(unittest.TestCase):
    """Test suite for the Fellow Model"""

    def test_created_fellow_successfully(self):
        new_fellow = Fellow(fname='Van', lname='Rossum')
        self.assertTrue(new_fellow)
        self.assertEqual(new_fellow.fname, 'Van')
        self.assertEqual(new_fellow.lname, 'Rossum')
        self.assertEqual(new_fellow.role, 'fellow')
        self.assertIsInstance(new_fellow, Person)
        self.assertNotIsInstance(new_fellow, Staff)
        self.assertIsInstance(new_fellow, Fellow)


class TestStaffClass(unittest.TestCase):
    """Test suite for the Staff Model"""

    def test_created_staff_successfully(self):
        new_staff = Staff(fname='Lanre', lname='Ogunmefun')
        self.assertTrue(new_staff)
        self.assertEqual(new_staff.fname, 'Lanre')
        self.assertEqual(new_staff.lname, 'Ogunmefun')
        self.assertEqual(new_staff.role, "staff")
        self.assertIsInstance(new_staff, Person)
        self.assertNotIsInstance(new_staff, Fellow)
        self.assertIsInstance(new_staff, Staff)


if '__name__' == '__main__':
    unittest.main()
