#!/usr/bin/env python

import sys
import unittest
from testcontext import Dojo


class TestReallocatePerson(unittest.TestCase):
    """Test suite for the reallocate person functionality"""

    def setUp(self):
        self.dojo = Dojo()

    def test_index_id_room(self):
        self.dojo.reallocate_person(1, 'Blue')
        result = sys.stdout.getvalue().strip()
        self.assertEqual(result, 'Id/Room_Name not found!')

    def test_not_reallocate_to_present_room(self):
        self.dojo.create_room('office', ['Orion'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.reallocate_person(1, 'ORION')
        result = sys.stdout.getvalue().strip()
        self.assertEqual(
            result[147:], 'You cannot reallocate person to current room.')

    def test_reallocate_fellow_staff_with_office(self):
        self.dojo.create_room('office', ['Naples'])
        self.dojo.add_person('brian', 'houston', 'fellow')
        self.dojo.add_person('ben', 'ayade', 'staff')
        fellow = self.dojo.people[0]
        staff = self.dojo.people[1]
        self.assertEqual(fellow.office, 'NAPLES')
        self.assertEqual(staff.office, 'NAPLES')
        self.dojo.create_room('office', ['Vienna'])
        self.dojo.reallocate_person(1, 'Vienna')
        self.dojo.reallocate_person(2, 'Vienna')
        self.assertEqual(fellow.office, 'VIENNA')
        self.assertEqual(staff.office, 'VIENNA')

    def test_reallocate_fellow_staff_with_no_office(self):
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.add_person('bayo', 'emmanuel', 'staff')
        fellow = self.dojo.people[0]
        staff = self.dojo.people[1]
        self.dojo.create_room('office', ['Blue'])
        self.assertFalse(fellow.office)
        self.assertFalse(staff.office)
        self.dojo.reallocate_person(1, 'Blue')
        self.dojo.reallocate_person(2, 'Blue')
        self.assertEqual(fellow.office, 'BLUE')
        self.assertEqual(staff.office, 'BLUE')

    def test_cannot_reallocate_to_full_room(self):
        self.dojo.create_room('office', ['Orion'])
        self.dojo.add_person('vie', 'ajah', 'fellow')
        self.dojo.add_person('dave', 'ajah', 'fellow')
        self.dojo.add_person('vie', 'emma', 'fellow')
        self.dojo.add_person('sojay', 'ajah', 'fellow')
        self.dojo.add_person('vie', 'beor', 'fellow')
        self.dojo.add_person('victor', 'anichebe', 'staff')
        self.dojo.add_person('kuti', 'mane', 'fellow')
        fellow = self.dojo.people[6]
        self.assertFalse(fellow.office)

    def test_invalid_person_id(self):
        self.dojo.add_person('ladi', 'adeniran', 'staff')
        self.dojo.create_room('office', ['Mane'])
        self.dojo.reallocate_person('1', 'orion')
        msg = sys.stdout.getvalue().strip()
        self.assertEqual(msg[130:], 'Person cannot be reallocated the room')

    def tearDown(self):
        del self.dojo
        