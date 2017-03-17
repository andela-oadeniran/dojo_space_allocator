#!/usr/bin/env python

import linecache
import unittest
import sys
from testcontext import Dojo
from testcontext import expanduser


class TestPrintRoom(unittest.TestCase):
    """Test suite for the print_room functionality"""

    def setUp(self):
        self.dojo = Dojo()

    def test_print_room_when_no_rooms(self):
        self.dojo.print_room('Blue')
        value = sys.stdout.getvalue().strip()
        self.assertEqual(value, 'BLUE not a room in Dojo.')

    def test_print_room_invalid_room(self):
        self.dojo.print_room('Valor')
        value = sys.stdout.getvalue().strip()
        self.assertEqual(value, 'VALOR not a room in Dojo.')

    def test_print_room_valid_empty_room(self):
        self.dojo.create_room('living_space', ['Maze'])
        self.dojo.print_room('Maze')
        result = sys.stdout.getvalue().strip()
        self.assertEqual(result[61:], 'MAZE currently has no occupant(s)!')

    def test_print_room_with_office_occupants(self):
        self.dojo.create_room('office', ['Blue'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.add_person('ab', 'soul', 'staff')
        self.dojo.print_room('Blue')
        result = sys.stdout.getvalue().strip()
        self.assertTrue(result)
        self.assertEqual(
            result[226:], 'Ladi Adeniran (FELLOW), Ab Soul (STAFF)')

    def test_print_room_with_living_space_occupants(self):
        self.dojo.create_room('living_space', ['orion'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        self.dojo.print_room('Orion')
        result = sys.stdout.getvalue().strip()
        self.assertEqual(result[185:], 'Ladi Adeniran (FELLOW)')

    def tearDown(self):
        del self.dojo


class TestPrintAllocations(unittest.TestCase):
    """This test suite tests the Print Allocations functionality."""

    def setUp(self):
        self.dojo = Dojo()
        self.HOME_DIR = expanduser('~')

    def test_print_allocations_when_no_room(self):
        self.dojo.print_allocations()
        result = sys.stdout.getvalue().strip()
        self.assertEqual(result, 'There are currently no rooms in Dojo.')

    def test_print_allocations_to_screen(self):
        self.dojo.create_room('office', ['idanre'])
        self.dojo.print_allocations()
        result = sys.stdout.getvalue().strip()
        self.assertTrue(result)
        self.assertEqual(result[104:], 'IDANRE has no occupants')

    def test_print_allocations_to_file(self):
        # test that file is valid and was written into.
        self.dojo.create_room('office', ['Blue'])
        self.dojo.add_person('ladi', 'ade', 'fellow')
        result = self.dojo.print_allocations('allocations')
        self.assertTrue(result)
        file_name = self.HOME_DIR + '/.dojo_data/allocations.txt'
        self.assertEqual(result, file_name)
        room_name = linecache.getline(result, 1).strip()
        allocations_line = linecache.getline(result, 3).strip()
        self.assertEqual(room_name, 'BLUE office')
        self.assertEqual(allocations_line, 'Ladi Ade (FELLOW)')

    def tearDown(self):
        del self.dojo


class TestPrintUnallocated(unittest.TestCase):
    """Test suite for the print_unallocated dojo function"""

    def setUp(self):
        self.dojo = Dojo()
        self.HOME_DIR = expanduser('~')

    def test_print_unallocated_for_no_people(self):
        result = self.dojo.print_unallocated()
        self.assertTrue(result)
        self.assertEqual(result, 'No person in the System Yet!')

    def test_print_no_unallocated_person(self):
        self.dojo.create_room('office', ['QB'])
        self.dojo.add_person('nas', 'escobar', 'fellow')
        result = self.dojo.print_unallocated()
        self.assertFalse(result)

    def test_print_unallocated_to_screen(self):
        self.dojo.add_person('rukky', 'remy', 'staff')
        self.dojo.print_unallocated()
        result = sys.stdout.getvalue().strip()
        self.assertTrue(result)
        self.assertEqual(result[108:128], '1 Rukky Remy (STAFF)')

    def test_print_unallocated_to_file(self):
        self.dojo.add_person('ric', 'hassani', 'fellow')
        value = self.dojo.print_unallocated('unallocated.txt')
        self.assertTrue(value)
        filename = self.HOME_DIR + '/.dojo_data/unallocated.txt'
        self.assertEqual(value, filename)
        unallocated_line1 = linecache.getline(value, 1).strip()
        unallocated_line2 = linecache.getline(value, 2).strip()
        self.assertEqual(
            unallocated_line1, '(ID) UNALLOCATED LIST OFFICE SPACE')
        self.assertEqual(
            unallocated_line2, '1 Ric Hassani (FELLOW)')

    def test_valid_people_id(self):
        self.dojo.add_person('remy', 'ma', 'staff')
        self.dojo.add_person('travis', 'greene', 'staff')
        self.dojo.add_person('temmy', 'orwase', 'fellow')
        self.dojo.people_id()
        result = sys.stdout.getvalue().strip()
        self.assertTrue(result)

    def tearDown(self):
        del self.dojo


if '__name__' == '__main__':
    unittest.main()

