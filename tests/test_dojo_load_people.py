#!/usr/bin/env python

from testcontext import Dojo
import unittest


class TestLoadPeople(unittest.TestCase):
    '''Test suite for the load people from text file function'''

    def setUp(self):
        self.dojo = Dojo()

    def test_load_people_from_file_successfully(self):
        result = self.dojo.people
        self.assertFalse(result)
        self.dojo.load_people('people.txt')
        result1 = self.dojo.people
        self.assertTrue(result1)
