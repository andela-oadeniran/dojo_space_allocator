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


class TestPrintRoom(unittest.TestCase):
    """Test suite for the print_room functionality"""

    def setUp(self):
        self.dojo = Dojo()
        self.print_room = self.dojo.print_room('blue')
        screen

    def test_print_room_successfully(self):
     
        captured_screen_message = sys.stdout().getvalue().strip()
        print (captured_screen_message)
        self.assertTrue(captured_screen_message)
        self.assertEqual('', captured_screen_message)

if '__name__' == '__main__':
    unittest.main()
