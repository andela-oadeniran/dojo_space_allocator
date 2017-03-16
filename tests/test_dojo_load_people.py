#!/usr/bin/env python

import os
import shutil
import unittest
from testcontext import Dojo
from testcontext import Dojo
from testcontext import expanduser


class TestLoadPeople(unittest.TestCase):
    '''Test suite for the load people from text file function'''

    def setUp(self):
        self.dojo = Dojo()
        self.HOME = expanduser('~')
        self.DATA_DIR = self.HOME + '/.dojo_data/'
        source = os.path.join(os.path.dirname(__file__), 'people.txt')
        print(source)
        if os.path.exists(self.DATA_DIR):
            shutil.copy(source, self.DATA_DIR)
        else:
            os.mkdir(self.DATA_DIR)
            shutil.copy(source, self.DATA_DIR)

    def test_load_people_from_file_successfully(self):
        result = self.dojo.people
        self.assertFalse(result)

        self.dojo.load_people('people.txt')
        result1 = self.dojo.people
        self.assertTrue(result1)
