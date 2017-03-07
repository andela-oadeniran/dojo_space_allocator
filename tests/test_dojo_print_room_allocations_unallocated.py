#!/usr/bin/env python

import os
import sys
dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)

import unittest
from dojo import Dojo
from os.path import expanduser
import linecache



class TestPrintRoom(unittest.TestCase):
    """Test suite for the print_room functionality"""

    def setUp(self):
        self.dojo = Dojo()

    def test_print_room_when_no_rooms(self):
        result = self.dojo.print_room('Blue')
        self.assertEqual(result, 'No rooms in Dojo.' )

    def test_print_room_invalid_room(self):
        self.dojo.create_room('office', ['orion'])
        self.assertEqual(self.dojo.print_room('blue'), 'Room name not in session.')
    
    def test_print_room_valid_empty_room(self):
        self.dojo.create_room('living', ['Maze'])
        result = self.dojo.print_room('Maze')
        self.assertEqual(result, 'MAZE currently has no occupant(s)')

    def test_print_room_with_office_occupants(self):
        self.dojo.create_room('office', ['Blue'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow' )
        self.dojo.add_person('ab', 'soul', 'staff')
        result = self.dojo.print_room('Blue')
        self.assertTrue(result)
        self.assertEqual(result, 'Ladi Adeniran (FELLOW), Ab Soul (STAFF)')

    def test_print_room_with_living_occupants(self):
        self.dojo.create_room('living', ['orion'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        result = self.dojo.print_room('Orion')
        self.assertTrue (result)
        self.assertEqual(result, 'Ladi Adeniran (FELLOW)')

    def tearDown(self):
        del self.dojo

class TestPrintAllocations(unittest.TestCase):
    """This test suite tests the Print Allocations functionality."""

    def setUp(self):
        self.dojo = Dojo()

    def test_print_allocations_when_no_room(self):
        result = self.dojo.print_allocations()
        self.assertTrue(result)
        self.assertEqual(result, 'There are currently no rooms in Dojo.')

    def test_print_allocations_to_screen(self):
        self.dojo.create_room('office', ['idanre'])
        result = self.dojo.print_allocations()
        self.assertTrue(result)
        self.assertEqual(result, 'Successfully printed allocations to screen')

    def test_print_allocations_to_file(self):
        # test that file is valid and was written into.
        self.dojo.create_room('office', ['Blue'])
        self.dojo.add_person ('ladi', 'ade', 'fellow')
        result = self.dojo.print_allocations('allocations.txt')
        self.assertTrue(result)
        home = expanduser('~')
        file_name = home + '/.dojo_data/allocations.txt'
        self.assertEqual(result, file_name )
        room_name = linecache.getline(result, 1).strip()
        allocations_line = linecache.getline(result, 3).strip()
        self.assertEqual(room_name, 'BLUE')
        self.assertEqual(allocations_line, 'Ladi Ade')

    def tearDown(self):
        del self.dojo

class TestPrintUnallocated(unittest.TestCase):
    """Test suite for the print_unallocated dojo function"""
    def setUp(self):
        self.dojo = Dojo()

    def test_print_unallocated_for_no_people(self):
        result = self.dojo.print_unallocated()
        self.assertTrue(result)
        self.assertEqual(result, 'No person in the System Yet!')

    def test_print_no_unallocated_person(self):
        self.dojo.create_room('office', ['QB'])
        self.dojo.add_person('nas','escobar', 'fellow')
        result = self.dojo.print_unallocated()
        self.assertFalse(result)

    def test_print_unallocated_to_screen(self):
        self.dojo.add_person('rukky', 'remy', 'staff')
        result = self.dojo.print_unallocated()
        self.assertTrue(result)
        self.assertEqual(result, 'Printed Allocation')

    def tearDown(self):
        del self.dojo





if '__name__' == '__main__':
    unittest.main()

