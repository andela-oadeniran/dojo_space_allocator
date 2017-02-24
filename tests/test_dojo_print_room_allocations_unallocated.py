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

    def test_print_room_successfully(self):
        dojo = Dojo()
        new_office = dojo.create_room('office', ['conf'])
        new_fellow = dojo.add_person('Troy', 'Kansas', 'fellow')
        output = dojo.print_room('conf')
        print(output)
        # assert that what is printed when print_room conference_hall is
        # new_fellow and new_staff names
        self.assertEqual('{0}'.format(output[0]), 'Troy Kansas')

# class TestPrintAllocation(unittest.TestCase):
# 	"""Test suite for the print_allocation functionality"""
# 	def test_print_allocations_to_file_successful(self):
# 		dojo = Dojo()
# 		new_office1 = dojo.create_room('office', ['White_House'])
# 		new_fellow1 = dojo.add_person('Maine', 'Minesota', 'fellow')
# 		#assert sys.stdout is properly formatted
# 		expected_text = '{0}\n-------------------\
# 		-----------------\n{1}\n\n'.format('WHITE_HOUSE', 'Maine Minesota')
# 		output_text =  dojo.print_allocations()


# class TestPrintUnallocated (unittest.TestCase):
# 	"""Test suite for the print_unallocated functionality"""

# 	def test_print_unallocated_to_file_successfully(self):
# 		dojo = Dojo()


if '__name__' == '__main__':
    unittest.main()
