#!bin/python3*
""" comment here"""
import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(modelsdir)
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from room import Room
import unittest


class TestCreateRoom(unittest.TestCase):
    """Write Docstring here """
    def test_create_room_successfully(self):
        new_class = Room ()
        initial_room_count = len(new_class.all_rooms)
        blue_office = Room.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
    # def test_create




if '__name__' == '__main__':
	unittest.main()
