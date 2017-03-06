#!/usr/bin/env python

import os
import sys
dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)


from dojo import Dojo
from models.fellow import Fellow
from models.staff import Staff
from models.living import LivingSpace
from models.office import Office
import unittest


class TestCreateRoom(unittest.TestCase):
    """Write Docstring here """

    def test_created_office_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        blue_office = dojo.create_room("office", ['BLUE'])
        value = Dojo.app_session['room']['BLUE']
        self.assertTrue(value)
        self.assertEqual(value.name, 'BLUE')
        self.assertEqual(value.purpose, 'office')
        capture_print = sys.stdout.getvalue().strip()
        self.assertEqual(capture_print, 'An Office called Blue has been successfully created!')
        new_room_count = len(dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_created_living_space_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        orange_living_space = dojo.create_room('living', ['ORANGE'])
        value1 = Dojo.app_session['room']['ORANGE']
        self.assertTrue(value1)
        self.assertEqual(value1.name, 'ORANGE')
        self.assertEqual(value1.purpose, 'living')
        capture_print = sys.stdout.getvalue().strip()
        self.assertEqual(capture_print, 'A Living Space called Orange has been successfully created!')
        new_room_count = len(dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
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
        amigo_office = dojo.create_room('office', ['amigo', 'amigo'])
        new_room_count = len(dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_create_room_is_only_for_offices_living_spaces(self):
        dojo = Dojo()
        other_pupose_room = dojo.create_room('kitchen', ['Puerto'])
        capture_print = sys.stdout.getvalue().strip()
        self.assertEqual(capture_print[0:24], 'The Room type is invalid')


class TestAddPerson(unittest.TestCase):
    """ The test suite for the Dojo Method to Add people"""

    def test_fellow_staff_added_successfully(self):
        dojo = Dojo()
        new_fellow = dojo.add_person('Ladi', 'Adeniran', 'Fellow')
        value2 = Dojo.app_session['person'][1]
        self.assertTrue(value2)
        self.assertEqual('{0} {1}'.format(value2.fname, value2.lname), 'Ladi Adeniran')
        self.assertEqual(value2.role, 'fellow')
        capture_print1 = sys.stdout.getvalue()
        self.assertEqual(capture_print1[0:48], 'Fellow Ladi Adeniran has been successfully added')
        new_staff = dojo.add_person('Joshua', 'Ezekiel', 'staff')
        value3 = Dojo.app_session['person'][2]
        self.assertTrue(value3)
        self.assertEqual(value3.fname, 'Joshua')
        self.assertTrue(value3.role, 'staff')

    def test_fellow_staff_rooms(self):
        dojo = Dojo()
        new_office = dojo.create_room('office', ['OPUS'])
        new_living = dojo.create_room('living', ['OLYMPUS'])
        fellow = dojo.add_person('Damisi', 'Otoloye', 'fellow', 'y')
        staff = dojo.add_person('bayo', 'adesanya','staff')
        value4 = Dojo.app_session['person'][3]
        value5 = Dojo.app_session['person'][4]
        self.assertEqual(value4.office, 'OPUS')
        self.assertEqual(value4.living_space, 'OLYMPUS')


if '__name__' == '__main__':
    unittest.main()
