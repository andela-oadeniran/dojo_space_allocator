#!/usr/bin/env python
# import modules and the models and db directory to the app's entry.

import os
import sys

dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './db'))
modelsdir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), './models'))

sys.path.append(dbdir)
sys.path.append(modelsdir)


import re

from db.db import Db
from models.office import Office
from models.living import LivingSpace
from models.staff import Staff
from models.fellow import Fellow


# The Dojo class contains the application logic and direct interaction
class Dojo(object):
    """ The Dojo class Docstring"""
    app_session = {'room': [], 'person': []}
    all_rooms = []
    people = []
    # room_names are unique and are used as the room identifier
    room_keys = []
    # people's names might not be unque but the ids here are.
    people_keys = []

    def __init__(self):
        pass

    def create_room(self, purpose, room_names):
        self.app_session = Dojo.app_session
        self.all_rooms = Dojo.all_rooms
        self.people = Dojo.people
        self.room_keys = Dojo.room_keys
        """ check if the purpose is either living or an office and also check for uniqueness"""
        if purpose.lower() in ('office', 'living'):
            if purpose.lower() == 'office':
                for index, room_name in enumerate(room_names):
                    if (room_name in Dojo.room_keys):
                        print('Room name already exists. Use a different name')
                    else:
                        room_key = room_name
                        room_name = Office(room_name)
                        Dojo.all_rooms.append(room_name)
                        Dojo.app_session['room'].append({room_key: room_name})
                        Dojo.room_keys.append(room_key)
                        # print(self.room_keys)
                        print(
                            "An Office called {0} has been successfully created!".format(room_key))
                # print(len(self.all_rooms))
                return room_name
            else:
                for index, room_name in enumerate(room_names):
                    if (room_name in Dojo.room_keys):
                        print("Room name already exists, Use a different name")
                    else:
                        room_key = room_name
                        room_name = LivingSpace(room_name)
                        Dojo.all_rooms.append(room_name)
                        Dojo.app_session['room'].append({room_key: room_name})
                        Dojo.room_keys.append(room_key)
                        print(
                            "A Living Space called {0} has been successfully created!".format(room_key))
                        return room_name
        else:
            print('Dojo contains Offices and Living Spaces ')

    def add_person(self, fname, lname, role, wants_accommodation='n'):
        self.people_keys = Dojo.people_keys
        if role.lower() in ('fellow', 'staff'):
            # FELLOW CLASS
            if role.lower() == 'fellow':
                # Improve on this and check with user before having duplicate names
                # 001,002 etc implement that
                person_name = "{0} {1}".format(fname, lname)
                fellow_name = person_name
                fellow_name = Fellow(fname, lname, wants_accommodation)
                print('Fellow {0} has been successfully added.'.format(
                    person_name))
                if wants_accommodation == 'n':
                    for index, room in enumerate(Dojo.all_rooms):
                        if (room.purpose == 'office') and (check_room_size(room)):
                            fellow_name.office = add_person_to_room(fellow_name, room)
                            print(fellow_name.office)
                            break
                    else:
                        print('I guess we need more Offices')
                else:
                    for index, room in enumerate(Dojo.all_rooms):
                        if(room.purpose == 'office'):
                            if check_room_size(room):
                                fellow_name.office = add_person_to_room(
                                    fellow_name, room)
                                break

                    else:
                        print('I guess we need more Offices')
                    for index, room in enumerate(Dojo.all_rooms):
                        if (room.purpose == 'living'):
                            if check_room_size(room):
                                fellow_name.living_space = add_person_to_room(
                                    fellow_name, room)
                                break
                    else:
                        print(
                            'You have been placed on the waiting list as we have no rooms yet')

                Dojo.people.append(fellow_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'].append({person_key: fellow_name})
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)

                return fellow_name
            # STAFF CLASS
            else:
                person_name = "{0} {1}".format(fname, lname)
                staff_name = person_name
                staff_name = Staff(fname, lname)

                for index, room in enumerate(Dojo.all_rooms):
                    if (room.purpose == 'office') and (check_room_size(room)):
                        staff_name.office = add_person_to_room(
                            staff_name, room)

                    else:
                        print('I guess we need more Offices')

                Dojo.people.append(staff_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'].append({person_key: staff_name})
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)
                print('Staff {0} has been successfully added.'.format(
                    person_name))
                return staff_name

        else:
            print('You can only add fellows and staff')

    def print_room(self, room_name):
        for index, room in enumerate(Dojo.all_rooms):
            if room.name == room_name:
                if room.occupants:
                    print(room.occupants)
                    return room.occupants
                else:
                    print("This room has no occupants yet")

    def print_allocations(self, to_file='n'):
        if not (to_file.endswith('.txt')):
            for index, room in enumerate(Dojo.all_rooms):
                if (room.occupants):
                    members = ', '.join(str(person).upper() for person in room.occupants)
                    text = '{0}\n------------------------------------\n{1}\n\n'.format(room.name.upper(), members)
                    print(text)
                    return text
                else:
                    text = '{0} \n -----------------------------\n {0} is empty\n\n'.format(room.name.upper())
                    print(text)
                    return text
        else:
            for index, room in enumerate(Dojo.all_rooms):
                if (room.occupants):
                    print("got here")
                    members = ', '.join(str(person).upper() for person in room.occupants)
                    text = '{0}\n------------------------------------\n{1}\n\n'.format(room.name.upper(), members)
                    file = open(to_file, 'a')
                    file.write(text)
                    file.close()
                    print(text)
                    return text
                else:
                    text = '{0} \n -------------------------- \n {0} is empty\n\n'.format(room.name.upper())
                    print(text)
                    return text


    def reallocate_person(self, person_name, room_name):
        pass

    def load_people(self):
        pass

    def save_state(self):
        pass

    def load_state(self, db_sql):
        pass


#
#       FUNCTION NAME                   FUNCTION USE
#
#
#
#

def add_person_to_room(person, room):
    room.occupants.append(person)
    return room.name


def check_room_size(room):
    if len(room.occupants) < room.max_size:
        return True
    else:
        return False


dojo = Dojo()
blue_office =  dojo.create_room('office', ['Blue'])
# dojo.print_room('Blue')
# orange_living_space = dojo.create_room('living', ['Orange'])
new_fellow = dojo.add_person('ladi', 'Adeniran', 'fellow')
# new_staff = dojo.add_person('Oladipup', 'Adeni', 'staff')
# new_staff = dojo.add_person('Oladipu', 'Adeni', 'fellow', 'y')
# new_staff = dojo.add_person('Oladip', 'Adeni', 'fellow')
# new_staff = dojo.add_person('Oladi', 'Adeni', 'fellow')
# new_staff = dojo.add_person('Olad', 'Adeniran', 'fellow')
# new_staff = dojo.add_person('Ola', 'Adeni', 'fellow')
dojo.print_allocations('allocations.txt')
# print()
# print()
# dojo.print_room('Blue')
# output = dojo.print_room('Blue')
# print(output)
# dojo.print_room('Orange')
# print(new_fellow.office)
# print(new_fellow.living_space)
# print(blue_office.occupants[0].fname)
# print(orange_living_space.occupants[0].fname)
# print(len(blue_office.occupants))
# print(len(orange_living_space.occupants))
# print(blue_office.occupants)
# print(new_fellow.office)
# print(new_fellow.living_space)
