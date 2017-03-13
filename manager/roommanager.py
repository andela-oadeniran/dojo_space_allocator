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

    # # @clsmethod
    # def create_room(self, room_type, room_name):
    #     room_class = self.return_living_office_class(room_name)
    #     room = room_class(room_name)
    #     return room

    # def create_office(self, room_name):
    #     '''this helps create an Office object'''
    #     office = Office(room_name.upper())
    #     return office

    # def create_living_space(self, room_name):
    #     '''This creates the a living space object'''
    #     living_space = LivingSpace(room_name.upper())
    #     return living_space

    def check_room_name_uniqueness(self, room_name, rooms_list):
        '''This checks for room uniqueness'''
        return True if room_name.upper() in rooms_list else False

    def add_room_to_session(self, room, rooms_list):
        '''This adds the room object to the Application session'''
        rooms_list.append(room)
        return rooms_list

    def add_person_to_room(self, room, person):
        '''This adds a person istance to an existing room instance'''
        room.occupants.append(person)
        return room

    def string_room_occupants(self, room):
        return str(', '.join(room.occupants)) if room.occupants else False

    def get_available_rooms(self, room_type, room_list):
        available_rooms = [room for room in room_list if room.room_type ==
                           room_type and len(room.occupants) < room.max_size]
        if available_rooms:
            room = random.choice(available_rooms)
            return room
        else:
            return None





