#!/usr/bin/env/python

import random
from manager_context import LivingSpace
from manager_context import Office


class RoomManager():
    '''
    This handles everything that a room is supposed to do.
    '''

    def __init__(self):
        pass

    def check_valid_room_type(self, room_type):
        '''this checks for the validity of room_type given'''
        if room_type.lower() in ('living', 'office'):
            return room_type
        else:
            raise TypeError

    def check_room_name(self, room_name):
        if room_name.strip():
            return True
        else:
            raise ValueError

    # @staticmethod
    def return_living_office_class(self, room_type):
        return Office if room_type.lower() == 'office' else LivingSpace

    def check_room_name_uniqueness(self, room_name, rooms_list):
        '''This checks for room uniqueness'''
        rooms_names = [str(room) for room in rooms_list]
        if room_name.upper() in rooms_names:
            return True
        else:
            False

    def add_room_to_session(self, room, rooms_list):
        '''This adds the room object to the Application session'''
        rooms_list.append(room)
        return rooms_list

    def add_person_to_room(self, room, person):
        '''This adds a person istance to an existing room instance'''
        room.occupants.append(person)
        return room

    def string_room_occupants(self, room):
        if room.occupants:
            occupants = [person.pname for person in room.occupants]
            return ', '.join(occupants)
        else:
            return False

    def get_available_room(self, room_type, room_list):
        available_rooms = [room for room in room_list if room.room_type ==
                           room_type and len(room.occupants) < room.max_size]
        if available_rooms:
            room = random.choice(available_rooms)
            return room
        else:
            return None

    def get_room_with_a_room_name(self, room_name, room_list):
        room = [room for room in room_list if room.name == room_name.upper()]
        return room[0]

    def print_text_to_file(self, to_file, text):
        with open(to_file, 'a') as allocations:
            allocations.write(text)

    def check_room_size(self, room):
        if len(room.occupants) < room.max_size:
            return True
        else:
            raise ValueError

    def check_person_can_be_in_room(self, room, person):
        if ((room.room_type == 'living') and
                (person.wants_accommodation.lower() != 'y')):
            raise TypeError
        else:
            return True

    def delete_person_from_room(self, room, person):
        if room:
            room.occupants.remove(person)
            return room.occupants
        else:
            return None







