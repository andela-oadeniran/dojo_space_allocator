#!/usr/bin/env python

import unittest
from testcontext import Room, Office, LivingSpace


class TestRoomClass(unittest.TestCase):
    """This represents the test suite for the Room Class
    """

    def test_create_room_successfully(self):
        new_room = Room(name='Blue', room_type='meeting room')
        self.assertTrue(new_room)
        self.assertIsInstance(new_room, Room)
        self.assertEqual(new_room.name, 'BLUE')
        self.assertEqual(new_room.room_type, 'meeting room')
        self.assertEqual(len(new_room.occupants), 0)

    def test_repr_name_rooms(self):
        new_room = Room(name='DWTW', room_type='kitchen')

        self.assertEqual(str(new_room), 'DWTW')


class TestOfficeClass(unittest.TestCase):
    """Tests for the Office class a subclass of the Room Class
    """

    def test_create_office_successfully(self):
        new_office = Office('Orange')
        self.assertEqual(new_office.name, 'ORANGE')
        self.assertIsInstance(new_office, Office)
        self.assertEqual(new_office.room_type, 'office')
        self.assertEqual(len(new_office.occupants), 0)
        self.assertIsInstance(new_office, Room)
        self.assertEqual(new_office.max_size, 6)

    def test_repr_name_living_spaces(self):
        new_room = Office('mane')
        self.assertEqual(str(new_room), 'MANE')


class TestLivingSpaceClass(unittest.TestCase):
    """Test cases for the LivingSpace Model
    """

    def test_create_living_space_successfully(self):
        new_living_space = LivingSpace('Orion')
        self.assertEqual(new_living_space.name, 'ORION')
        self.assertNotEqual(new_living_space.name, 'BLUE')
        self.assertEqual(new_living_space.room_type, 'living')
        self.assertIsInstance(new_living_space, Room)
        self.assertNotIsInstance(new_living_space, Office)
        self.assertEqual(len(new_living_space.occupants), 0)
        self.assertEqual(new_living_space.max_size, 4)

    def test_repr_name_living_spaces(self):
        new_room = LivingSpace('Ephesus')
        self.assertEqual(str(new_room), 'EPHESUS')



if '__name__' == '__main__':
    unittest.main()
