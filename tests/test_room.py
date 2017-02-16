#!/bin/python3*
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
        room = Room ('Office', 'Blue')
        # initial_room_count = len(new_class.all_rooms)
        # blue_office = Room.create_room("Blue", "office")
        self.assertTrue(room)
        self.assertEqual(room.room_name, 'Blue')
        self.assertEqual(room.room_type, 'Office')

        # new_room_count = len(my_class_instance.all_rooms)
        # self.assertEqual(new_room_count - initial_room_count, 1)

    # def test_create_room_is_only_office_living:
    # 	new_class = Room()





if '__name__' == '__main__':
	unittest.main()
