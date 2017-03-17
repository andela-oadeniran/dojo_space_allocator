# import modules

import sys
import unittest
from testcontext import Dojo


class TestSaveState(unittest.TestCase):
    ''' The test suite for the functionalities,
    save state and load state in the Dojo
    class'''

    def setUp(self):
        self.dojo = Dojo()

    def test_empty_session_not_persisted(self):
        self.dojo.save_state()
        result = sys.stdout.getvalue().strip()
        self.assertEqual(
            result, 'Session has no data to persist to the database.')

    def test_session_with_data_saved_successfully(self):
        self.dojo.create_room('office', ['Valala'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.add_person('pet', 'sampras', 'staff')
        self.dojo.save_state('test_dojo.db')
        result = sys.stdout.getvalue().strip()
        self.assertTrue(result)
        self.assertEqual(
            result[237:280], 'Your session has been saved to the database')

    def tearDown(self):
        del self.dojo


class TestLoadState(unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()

    def test_load_file_successfully(self):
        self.dojo.create_room('office', ['Valala'])
        self.dojo.add_person('ladi', 'adeniran', 'fellow')
        self.dojo.add_person('pet', 'sampras', 'staff')
        self.dojo.save_state('test_dojo.db')
        self.dojo.load_state('test_dojo.db')
        room = self.dojo.all_rooms[0]
        fellow = self.dojo.people[0]
        staff = self.dojo.people[1]
        self.assertEqual(room.name, 'VALALA')
        self.assertTrue(fellow.fname, 'Ladi')
        self.assertTrue(staff.fname, 'Pet')

    def test_handle_bad_db(self):
        self.dojo.append_valid_extension_to_data_path('bad', '.db')
        self.dojo.load_state('bad.db')
        result = sys.stdout.getvalue().strip()
        self.assertEqual(result, 'Does not exist or Invalid')


