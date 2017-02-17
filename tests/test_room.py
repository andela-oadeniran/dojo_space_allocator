#!/usr/bin/env python

""" comment here"""

import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from room import Room
from office import Office
from living import LivingSpace
import unittest


class TestRoomClass(unittest.TestCase):
    """This represents the test suite for the Room Class
    """
    def test_created_room_successfully(self):
        new_room = Room(name='Blue', purpose='meeting room')
        self.assertTrue(new_room, msg='A new room was created')
        self.assertIsInstance(new_room, Room, msg='Blue is an instance of the Room Class')
        self.assertEqual(new_room.name, 'Blue')
        self.assertEqual(new_room.purpose, 'meeting room')
        self.assertEqual(len(new_room.occupants), new_room.size)


class TestOfficeClass(unittest.TestCase):
    """Tests for the Office class a subclass of the Room Class
    """
    def test_created_office_successfully(self):
        new_office = Office('Orange')
        self.assertEqual(new_office.name, 'Orange')
        self.assertIsInstance(new_office, Office)
        self.assertEqual(new_office.purpose, 'office', msg="assert the Office class creates only offices")
        self.assertEqual(len(new_office.occupants), new_office.size)
        self.assertIsInstance(new_office, Room, msg="Room class is a super class of the office class")
        self.assertEqual(new_office.max_size, 6)


class TestLivingSpaceClass(unittest.TestCase):
    """Test cases for the LivingSpace Model
    """
    def test_created_living_space_successfully(self):
        new_living_space = LivingSpace('Orion')
        self.assertEqual(new_living_space.name, 'Orion')
        self.assertNotEqual(new_living_space.name, 'Blue')
        self.assertEqual(new_living_space.purpose, 'living')
        self.assertIsInstance(new_living_space, Room, msg="The Room class is a super class of the LivingSpace")
        self.assertNotIsInstance(new_living_space, Office, msg='livingSpace doesn\'t inherit from Office ')
        self.assertEqual(len(new_living_space.occupants), new_living_space.size)
        self.assertEqual(new_living_space.max_size, 4)





if '__name__' == '__main__':
	unittest.main()
