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
    app_session = {'room': {}, 'person': {}}
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
                        print('Room name already exists. Use a different name\n')
                    else:
                        room_key = room_name
                        room_name = Office(room_name)
                        Dojo.all_rooms.append(room_name)
                        Dojo.app_session['room'][room_key] = room_name
                        Dojo.room_keys.append(room_key)
                        print(
                            "An Office called {0} has been successfully created!\n".format(room_key))
            else:
                for index, room_name in enumerate(room_names):
                    if (room_name in Dojo.room_keys):
                        print("Room name already exists, Use a different name")
                    else:
                        room_key = room_name
                        room_name = LivingSpace(room_name)
                        Dojo.all_rooms.append(room_name)
                        Dojo.app_session['room'][room_key] = room_name
                        Dojo.room_keys.append(room_key)
                        print(
                            "A Living Space called {0} has been successfully created!\n".format(room_key))
                        # return room_name
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
                print('Fellow {0} has been successfully added.\n'.format(
                    person_name))
                if wants_accommodation != 'y':
                    for index, room in enumerate(Dojo.all_rooms):
                        if (room.purpose == 'office') and (check_room_size(room)):
                            fellow_name.office = add_person_to_room(
                                fellow_name, room)
                            print('{0} has been allocated the Office {1}'.format(fname, fellow_name.office))
                            break
                    else:
                        print('I guess we need more Offices')
                else:
                    for index, room in enumerate(Dojo.all_rooms):
                        if(room.purpose == 'office'):
                            if check_room_size(room):
                                fellow_name.office = add_person_to_room(
                                    fellow_name, room)
                                print('{0} has been allocated the Office {1}'.format(fname, fellow_name.office))
                                break

                    else:
                        print('I guess we need more Offices')
                    for index, room in enumerate(Dojo.all_rooms):
                        if (room.purpose == 'living'):
                            if check_room_size(room):
                                fellow_name.living_space = add_person_to_room(
                                    fellow_name, room)
                                print('{0} has been allocated the living space {1}'.format(fname, fellow_name.office))
                                break
                    else:
                        print(
                            'You have been placed on the waiting list as we have no rooms yet')

                Dojo.people.append(fellow_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'][person_key] = fellow_name
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)
                # return fellow_name

            # STAFF CLASS
            else:
                person_name = "{0} {1}".format(fname, lname)
                staff_name = person_name
                staff_name = Staff(fname, lname)
                print('Staff {0} has been successfully added.'.format(
                    person_name))


                for index, room in enumerate(Dojo.all_rooms):
                    if (room.purpose == 'office') and (check_room_size(room)):
                        staff_name.office = add_person_to_room(
                            staff_name, room)
                        print('{0} has been allocated the office {1}'.format(staff_name.fname, room.name))
                        break

                    else:
                        print('I guess we need more Offices')

                Dojo.people.append(staff_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'][person_key] = staff_name
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)

        else:
            print('You can only add fellows and staff\n')

    def print_room(self, room_name):
        if (Dojo.all_rooms):
            for index, room in enumerate(Dojo.all_rooms):
                if room.name == room_name:
                    if room.occupants:
                        print(room.occupants)
                        # return room.occupants
                        break
                    else:
                        print("This room has no occupants yet.\n")
                        break
            else:
                print ('{} not in Dojo'.format())
        else:
            print('No room in Dojo yet.')

    def print_allocations(self, to_file='n'):
        print (Dojo.all_rooms)
        if (Dojo.all_rooms):
            if not (to_file.endswith('.txt')):
                for index, room in enumerate(Dojo.all_rooms):
                    if (room.occupants):
                        members = ', '.join(str(person).upper()
                                            for person in room.occupants)
                        text = '{0}\n------------------------------------\n{1}\n\n'.format(
                            room.name.upper(), members)
                        print(text)
                        # return text
                    else:
                        text = '{0}\n-----------------------------\n{0} is empty\n\n'.format(
                            room.name.upper())
                        print(text)

            else:
                for index, room in enumerate(Dojo.all_rooms):
                    if (room.occupants):
                        members = ', '.join(str(person).upper()
                                            for person in room.occupants)
                        text = '{0}\n------------------------------------\n{1}\n\n'.format(
                            room.name.upper(), members)
                        file = open(to_file, 'a')
                        file.write(text)
                        file.close()
                        print('Successfully written the Allocations to {0}'.format(to_file))
                    else:
                        text = '{0}\n -------------------------- \n {0} is empty\n\n'.format(
                            room.name.upper())
        else:
            print('There are no rooms in Dojo yet\n')
    def print_unallocated(self, to_file='n'):
        if (Dojo.people):
            if not (to_file.endswith('.txt')):
                for index, person in enumerate(Dojo.people):
                    if not (person.office):
                        print('{0} needs an Office'.format(str(person).upper()))
                    if (person.role == 'fellow'):
                        if(person.wants_accommodation=='y'):
                            if not(person.living_space):
                                print('{0} needs a Living Space'.format(str(person).upper()))
            else:
                for index, person in enumerate(Dojo.people):
                    if not (person.office):
                        text = ('{0} needs an Office\n'.format(str(person).upper()))
                        file = open(to_file, 'a')
                        file.write(text)
                        file.close()
                    if (person.role == 'fellow'):
                        if(person.wants_accommodation=='y'):
                            if not(person.living_space):
                                text2 = ('{0} needs a Living Space\n'.format(str(person).upper()))
                                fl = open(to_file, 'a')
                                fl.write(text2)
                                fl.close()
        else:
            print('No person added yet')

    def people_id(self):
        print ('ID       PERSON')
        for index, person_key in enumerate(Dojo.people_keys):
            print ('{0}  {1}'.format(person_key, Dojo.people[index]))

    def reallocate_person(self, person_id, room_name):
        print (Dojo.all_rooms)
        if (person_id in Dojo.people_keys) and (room_name in Dojo.room_keys):
            room = Dojo.app_session['room'][room_name]
            person = Dojo.app_session['person'][person_id]
            if (check_room_size(room)):
                if room.purpose =='office':
                    if person.office:
                        delete_person_from_room(person, Dojo.app_session['room'][person.office])
                        person.office = add_person_to_room(person, room)
                        print('{0} has been allocated the office {1}'.format(person.fname, room.name))
                    else:
                        person.office = add_person_to_room(person, room)
                        print('{0} has been allocated the office {1}'.format(person.fname, room.name))
                else:
                    if person.role == 'fellow':
                        if person.wants_accommodation=='y':
                            if person.living_space:
                                delete_person_from_room(person, Dojo.app_session['room'][person.living_space])
                                person.living_space = add_person_to_room(person, room)
                                print('{0} has been allocated the living space {1}'.format(person.fname, room.name))
                            else:
                                person.living_space = add_person_to_room(person, room)
                                print('{0} has been allocated the living space {1}'.format(person.fname, room.name))
                    else:
                        print('You cannot add {} a Staff to a living Space.'.format(person.fname))

            else:
                print('You cannot Reallocate to a full Room')
        else:
            print ('Invalid Person Id or Room name')

    def load_people(self):
        file = open('people.txt')

        for line in file.readlines():
            values = line.split()
            if len(values) == 3:
                self.add_person(values[0], values[1], values[2])
            else:
                self.add_person(values[0],values[1], values[2], values[3])
        file.close()

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
def delete_person_from_room(person, room):
    # del(room.occupants(person))
    room.occupants.remove(person)

def check_room_size(room):
    if len(room.occupants) < room.max_size:
        return True
    else:
        return False


# dojo = Dojo()
# dojo.create_room('office', ['Blue'])
# print(Dojo.app_session['room'])
# print(Dojo.all_rooms)
# dojo.create_room('office', ['Blue', 'Green'])
# print(Dojo.app_session['room'])
# dojo.print_room('Blue')
# dojo.print_room('Blue')
# orange_living_space = dojo.create_room('living', ['Orange'])
# new_fellow = dojo.add_person('ladi', 'Adeniran', 'fellow')
# new_staff = dojo.add_person('Oladipup', 'Adeni', 'staff')
# new_staff = dojo.add_person('Oladipu', 'Adeni', 'fellow', 'y')
# new_staff = dojo.add_person('Oladip', 'Adeni', 'fellow')
# new_staff = dojo.add_person('Oladi', 'Adeni', 'fellow')
# new_staff = dojo.add_person('Olad', 'Adeniran', 'fellow')
# new_staff = dojo.add_person('Ola', 'Adeni', 'fellow')
# dojo.print_allocations()
# dojo.print_room('')
# print()
# dojo.print_room('Blue')
# dojo.print_room('Green')
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
# dojo.print_unallocated('unallocated.txt')
# dojo.people_id()
# dojo.create_room('office', ['Green'])
# dojo.reallocate_person(7, 'Green')
# dojo.print_allocations()
# dojo.print_room('Blue')
# dojo.print_room('Green')
# dojo = Dojo()
# dojo.load_people()