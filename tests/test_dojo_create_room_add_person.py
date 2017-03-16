#!/usr/bin/env python

import unittest
from testcontext import Dojo, RoomManager, PersonManager


class TestCreateRoom(unittest.TestCase):
    """Write Docstring here """

    def setUp(self):
        self.dojo = Dojo()
        self.room_manager = RoomManager()
        self.person_manager = PersonManager()

    def test_created_office_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room("office", ['BLUE'])
        value = self.room_manager.get_room_with_a_room_name(
            'Blue', self.dojo.all_rooms)
        self.assertTrue(value)
        self.assertEqual(value.name, 'BLUE')
        self.assertEqual(value.room_type, 'office')
        new_room_count = len(self.dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_created_living_space_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room('living_space', ['ORANGE'])
        value = self.room_manager.get_room_with_a_room_name(
            'orange', self.dojo.all_rooms)
        self.assertTrue(value)
        self.assertEqual(value.name, 'ORANGE')
        self.assertEqual(value.room_type, 'living_space')
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

    def test_max_office_size(self):
        self.dojo.create_room('office', ['MAZE'])
        room = self.room_manager.get_room_with_a_room_name(
            'Maze', self.dojo.all_rooms)
        self.assertEqual(room.max_size, 6)
        self.assertEqual(len(room.occupants), 0)

    def test_max_living_space_size(self):
        self.dojo.create_room('living_space', ['ORION'])
        room = self.room_manager.get_room_with_a_room_name(
            'orion', self.dojo.all_rooms)
        self.assertEqual(room.max_size, 4)
        self.assertEqual(len(room.occupants), 0)

    def test_max_limit_added_office(self):
        self.dojo.create_room('office', ['DEV'])
        room = self.room_manager.get_room_with_a_room_name(
            'Dev', self.dojo.all_rooms)
        self.assertEqual(len(room.occupants), 0)
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.add_person('ade', 'poju', 'staff')
        self.dojo.add_person('ginu', 'whyne', 'fellow')
        self.dojo.add_person('mark', 'anthony', 'fellow')
        self.dojo.add_person('anthony', 'hamilton', 'fellow')
        self.dojo.add_person('game', 'truce', 'fellow')
        self.dojo.add_person('saliu', 'bryan', 'fellow')
        self.dojo.add_person('zuck', 'beast', 'fellow')
        self.assertEqual(len(room.occupants), 6)

    def tearDown(self):
        del self.dojo
        del self.room_manager
        del self.person_manager


class TestAddPerson(unittest.TestCase):
    """Test suite for the add_person Dojo functonality
    """

    def setUp(self):
        self.dojo = Dojo()
        self.room_manager = RoomManager()
        self.person_manager = PersonManager()

    def test_create_fellow_successfully(self):
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        result = self.dojo.people[0]
        self.assertTrue(result)
        self.assertEqual(result.fname, 'Ladi')
        self.assertEqual(result.lname, 'Adeniran')
        self.assertEqual(result.role, 'fellow')

    def test_create_staff_successfully(self):
        self.dojo.add_person('Nas', 'Jones', 'staff')
        result = self.dojo.people[0]
        self.assertTrue(result)
        self.assertEqual(result.fname, 'Nas')
        self.assertEqual(result.lname, 'Jones')
        self.assertEqual(result.role, 'staff')

    def test_add_fellow_staff_to_office_successfully(self):
        self.dojo.create_room('office', ['Blue'])
        self.dojo.add_person('Ab', 'Soul', 'fellow')
        self.dojo.add_person('Jeremih', 'Camp', 'staff')
        fellow = self.dojo.people[0]
        staff = self.dojo.people[1]
        room = self.room_manager.get_room_with_a_room_name(
            'Blue', self.dojo.all_rooms)
        self.assertTrue(fellow)
        self.assertTrue(staff)
        self.assertEqual(fellow.office, 'BLUE')
        self.assertEqual(staff.office, 'BLUE')
        self.assertTrue(room.occupants)
        self.assertEqual(str(room.occupants[0]), 'Ab Soul')
        self.assertEqual(str(room.occupants[1]), 'Jeremih Camp')

    def test_add_fellow_to_living_space(self):
        self.dojo.create_room('living_space', ['Amity'])
        self.dojo.add_person('Jeremiah', 'Camp', 'fellow', 'y')
        fellow = self.dojo.people[0]
        room = self.room_manager.get_room_with_a_room_name(
            'Amity', self.dojo.all_rooms)
        self.assertEqual(fellow.living_space, 'AMITY')
        self.assertEqual(str(room.occupants[0]), 'Jeremiah Camp')

    def test_only_add_fellow_or_staff(self):
        self.dojo.add_person('Joshua', 'Emmsong', 'Engineer')
        engineer = self.dojo.people
        self.assertFalse(engineer)

    def test_staff_not_have_living_space(self):
        self.dojo.create_room('living_space', ['UPPERROOM'])
        self.dojo.add_person('ladi', 'adeniran', 'staff', 'y')
        staff = self.dojo.people[0]
        self.assertTrue(staff)
        self.assertEqual(staff.office, None)
        room = self.room_manager.get_room_with_a_room_name(
            'Upperroom', self.dojo.all_rooms)
        self.assertFalse(room.occupants)


if '__name__' == '__main__':
    unittest.main()
