
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
    def setUp(self):
        self.dojo = Dojo()

    def test_created_office_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room("office", ['BLUE'])
        value = self.dojo.app_session['room']['BLUE']
        self.assertTrue(value)
        self.assertEqual(value.name, 'BLUE')
        self.assertEqual(value.purpose, 'office')
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_created_living_space_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room('living', ['ORANGE'])
        value = self.dojo.app_session['room']['ORANGE']
        self.assertTrue(value)
        self.assertEqual(value.name, 'ORANGE')
        self.assertEqual(value.purpose, 'living')
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_created_multi_offices_or_living_spaces(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room('office', ['Orion', 'Dev', 'fly'])
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 3)

    def test_room_uniqueness(self):
        initial_room_count = len(self.dojo.all_rooms)
        amigo_office = self.dojo.create_room('office', ['amigo', 'amigo'])
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_create_room_is_only_for_offices_living_spaces(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room('kitchen', ['Puerto'])
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 0)

    def tearDown(self):
        del self.dojo

class TestAddPerson(unittest.TestCase):
    """Test suite for the add_person Dojo functonality"""
    def setUp(self):
        self.dojo = Dojo()

    def  test_create_fellow_successfully(self):
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        result = self.dojo.app_session['person'][1]
        self.assertTrue(result)
        self.assertEqual(result.fname, 'Ladi')
        self.assertEqual(result.lname, 'Adeniran')
        self.assertEqual(result.role, 'fellow')

    def test_create_staff_successfully(self):
        self.dojo.add_person('Nas', 'Jones', 'staff')
        result = self.dojo.app_session['person'][1]
        self.assertTrue(result)
        self.assertEqual(result.fname, 'Nas')
        self.assertEqual(result.lname, 'Jones')
        self.assertEqual(result.role, 'staff')

    def test_add_fellow_staff_to_office_successfully(self):
        self.dojo.create_room('office', ['Blue'])
        self.add_person('Ab', 'Soul', 'fellow')
        self.add_person('Jeremih', 'Camp', 'staff')
        fellow = self.dojo.app_session['person'][1]
        staff = self.dojo.app_session['person'][2]
        self.assertTrue(fellow)
        self.assertTrue(staff)



if '__name__' == '__main__':
    unittest.main()
