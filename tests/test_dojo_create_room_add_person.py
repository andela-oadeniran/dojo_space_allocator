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
        blue_office = dojo.create_room("office", ['Blue'])
        capture_print = sys.stdout.getvalue().strip()
        self.assertEqual(capture_print, 'An Office called Blue has been successfully created!')
        new_room_count = len(dojo.all_rooms)
        room_count_diff = new_room_count - initial_room_count
        self.assertEqual(room_count_diff, 1)

    def test_created_living_space_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        orange_living_space = dojo.create_room('living', ['Orange'])
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
    """The test suite for the  Dojo Method add_person"""

    def test_fellow_staff_added_successfully(self):
        dojo = Dojo()
        people_population = len(Dojo.people)
        new_fellow = dojo.add_person('Ladi', 'Adeniran', 'fellow', 'y')
        capture_print1 = sys.stdout.getvalue()
        # new_staff = dojo.add_person('Usman', 'Ibrahim', 'staff')
        # capture_print2 = sys.stdout.getvalue().strip()
        new_people_population = len(Dojo.people)
        people_population_diff = new_people_population - people_population
        print('here')
        # self.assertEqual(capture_print1[0:], 'Fellow Ladi Adeniran has been successfully added.')
        # self.assertEqual(people_population_diff, 1)


#     def test_added_person_to_room_successfully(self):
#         dojo = Dojo()
#         bayern_office = dojo.create_room('office', ['Bayern'])
#         zeus_living_space = dojo.create_room('living', ['Zeus'])
#         new_fellow = dojo.add_person('ladi', 'Adeniran', 'fellow', 'y')
#         self.assertEqual(new_fellow.office, 'Bayern')
#         self.assertEqual(new_fellow.living_space, 'Zeus')


# if '__name__' == '__main__':
#     unittest.main()
