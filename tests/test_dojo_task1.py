#!/usr/bin/env python

import os, sys
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
		new_office = dojo.create_room('office', ['conference_hall'])
		new_fellow = dojo.add_person('Troy', 'Kansas', 'fellow')
		new_staff = dojo.add_person('Didynius', 'Phillip', 'staff')
		output = dojo.print_room('conference_hall')
		print (output)
		# assert that what is printed when print_room conference_hall is new_fellow and new_staff names
		self.assertEqual('{0}'.format(output[0]), 'Troy Kansas')
		self.assertEqual('{0}'.format(output[1]), 'Didynius Phillip')

# class TestPrintAllocation(unittest.TestCase):
# 	"""Test suite for the print_allocation functionality"""
# 	def test_print_allocations_to_file_successful(self):
# 		dojo = Dojo()
# 		new_office1 = dojo.create_room('office', ['White_House'])
# 		new_fellow1 = dojo.add_person('Maine', 'Minesota', 'fellow')
# 		#assert sys.stdout is properly formatted


# class TestPrintUnallocated (unittest.TestCase):
# 	"""Test suite for the print_unallocated functionality"""

# 	def test_print_unallocated_to_file_successfully(self):
# 		dojo = Dojo()




if '__name__' == '__main__':
    unittest.main()