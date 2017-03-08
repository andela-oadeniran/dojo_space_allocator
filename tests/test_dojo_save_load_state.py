# import modules

import os
import sys
import unittest
import sqlite3

dojodir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(dojodir)
from dojo import Dojo

class TestSaveState(unittest.TestCase):
    ''' The test suite for the functionalities,
    save state and load state in the Dojo
    class'''

    def setUp(self):
    	self.dojo = Dojo()

    def test_empty_session_not_persisted(self):
    	result = self.dojo.save_state()
    	self.assertEqual(result, 'Session not persisted, No data in app_session')

    def test_session_with_data_save_successfully(self):
    	self.dojo.create_room('office', ['Valala'])
    	self.dojo.add_person('ladi', 'adeniran', 'fellow')
    	self.dojo.add_person('pet', 'sampras', 'staff')
    	result = self.dojo.save_state('test_dojo.db')
    	self.assertTrue(result)
    	self.assertEqual(result, 'data persisted')

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
        room = self.dojo.app_session['room']['VALALA']
        fellow = self.dojo.app_session['person'][1]
        staff = self.dojo.app_session['person'][2]
        self.assertEqual(room.name, 'VALALA')
        self.assertTrue(fellow.fname, 'Ladi')
        self.assertTrue(staff.fname, 'Pet')


    def test_handle_bad_db(self):
        home = os.path.expanduser('~')
        db_dir = home + '/.dojo_data/'
        if os.path.exists(db_dir):
            bad_db = db_dir + 'bad.db'
            bad_conn = sqlite3.connect(bad_db)
            bad_conn_close = bad_conn.close()
        else:
            os.mkdir(db_dir)
            bad_db = db_dir + 'bad.db'
            bad_conn = sqlite3.connect(bad_db)
            bad_conn.close()
        result = self.dojo.load_state('bad.db')
        self.assertEqual(result, 'Bad Database given')


