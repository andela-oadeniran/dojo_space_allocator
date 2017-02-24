#!/usr/bin/env python


import os
import sys
import unittest
modelsdir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)
from room import Room
from office import Office
from living import LivingSpace


class TestRoomClass(unittest.TestCase):
    """This represents the test suite for the Room Class
    """

    def test_create_room_successfully(self):
        new_room = Room(name='Blue', purpose='meeting room')
        self.assertTrue(new_room)
        self.assertIsInstance(new_room, Room)
        self.assertEqual(new_room.name, 'Blue')
        self.assertEqual(new_room.purpose, 'meeting room')
        self.assertEqual(len(new_room.occupants), 0)


class TestOfficeClass(unittest.TestCase):
    """Tests for the Office class a subclass of the Room Class
    """

    def test_create_office_successfully(self):
        new_office = Office('Orange')
        self.assertEqual(new_office.name, 'Orange')
        self.assertIsInstance(new_office, Office)
        self.assertEqual(new_office.purpose, 'office')
        self.assertEqual(len(new_office.occupants), 0)
        self.assertIsInstance(new_office, Room)
        self.assertEqual(new_office.max_size, 6)


class TestLivingSpaceClass(unittest.TestCase):
    """Test cases for the LivingSpace Model
    """

    def test_create_living_space_successfully(self):
        new_living_space = LivingSpace('Orion')
        self.assertEqual(new_living_space.name, 'Orion')
        self.assertNotEqual(new_living_space.name, 'Blue')
        self.assertEqual(new_living_space.purpose, 'living')
        self.assertIsInstance(new_living_space, Room)
        self.assertNotIsInstance(new_living_space, Office)
        self.assertEqual(len(new_living_space.occupants), 0)
        self.assertEqual(new_living_space.max_size, 4)


if '__name__' == '__main__':
    unittest.main()
