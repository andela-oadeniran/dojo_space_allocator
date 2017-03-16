#!/usr/bin/env python

# import modules. sys, os, models and db modules to the main application.
import os
from os.path import expanduser
import sqlite3
import pickle
import termcolor
from termcolor import cprint
from context import RoomManager
from context import PersonManager
from context import DojoDb

room_manager = RoomManager()
person_manager = PersonManager()


class Dojo(object):
    """
    The class contains all rooms and persons in the system and
    it is the main script for the application.
    """

    def __init__(self):
        # constructor method
        self.all_rooms = []
        self.people = []
        self.HOME = expanduser('~')
        self.DATA_DIR = self.HOME + '/.dojo_data/'

    def create_room(self, room_type, room_names):
        # The class calls on the room_manager methods to create rooms.
        try:
            room_manager.check_valid_room_type(room_type)
            room_class = room_manager.return_living_office_class(room_type)
            for room_name in room_names:
                room_manager.check_room_name(room_name)
                if not room_manager.check_room_name_uniqueness(room_name,
                                                               self.all_rooms):

                    room = room_class(room_name)
                    room_manager.add_room_to_session(room, self.all_rooms)
                    print('A/An {0} called {1} has been'
                          ' successfully created!'.format(
                              room_type, room_name.title()))
                else:
                    print('{} already exists!!!'.format(room_name))
        except TypeError:
            print('Invalid Room Type')
        except ValueError:
            print('Room Name Cannot be an Empty String')

    def add_person(self, fname, lname, role, wants_accommodation=None):
        ''' check role of the person supplied must either be a staff or a fellow
        if office is available add either to an office and if a fellow wants
        accommodation allocate to a living space if available '''
        try:
            person_manager.check_valid_person_role(role)
            person_manager.check_name_validity(fname, lname)
            person_class = person_manager.return_staff_fellow_class(role)
            person = person_class(fname, lname, wants_accommodation)
            person_manager.add_person_to_session(person, self.people)
            available_office = room_manager.get_available_room(
                'office', self.all_rooms)
            available_living_space = room_manager.get_available_room(
                'living_space', self.all_rooms)
            print('{0} {1} {2} has been successfully added.'.format(
                role.title(), fname.title(), lname.title()))
            if available_office:
                room_manager.add_person_to_room(available_office, person)
                person_manager.assign_person_room_name(
                    available_office, person)
                print('{0} has been allocated the office {1}'.format(
                    fname.title(), person.office.title()))
            else:
                print('No available office space')
            if ((person.role == 'fellow') and
                    person.wants_accommodation in ('y', 'Y')):
                if available_living_space:
                    room_manager.add_person_to_room(
                        available_living_space, person)
                    person_manager.assign_person_room_name(
                        available_living_space, person)
                    print('{0} has been allocated the living space {1}'.format
                          (fname.title(), person.living_space.title()))
                else:
                    print('No Available living space.')
        except TypeError:
            print('invalid type')
        except ValueError:
            print('invalid firstname and/or lastname')

    def print_room(self, room_name):
        # check if room exists in dojo
        if room_manager.check_room_name_uniqueness(
                room_name, self.all_rooms):
            room = room_manager.get_room_with_a_room_name(
                room_name, self.all_rooms)
            occupants = room_manager.string_room_occupants(room)
            if occupants:
                print(occupants)
                return occupants
            else:
                print('{} currently has no occupant(s)!'.format(
                    room_name.upper()))
                return '{} currently has no occupant(s)!'.format(
                    room_name.upper())
        else:
            print('{} not a room in Dojo'.format(room_name.upper()))
            return('{} not a room in Dojo.'.format(room_name.upper()))

    def print_allocations(self, to_file=None):
        ''' print_allocations take a key word argument to_file and defaults to 'n'
        This should be passed when user justs wants to print to stdout and'''
        if self.all_rooms:
            for room in self.all_rooms:
                occupants = room_manager.string_room_occupants(room)
                if occupants:
                    text = '{0} {1}\n{2}\n{3}'.format(room.name,
                                                      room.room_type,
                                                      '-' * 30, occupants)
                else:
                    text = '{0} ({1})\n{2}\n{0} has no occupants'.format(
                        room.name, room.room_type.title(), '-' * 30)
                if to_file:
                    to_file = self.append_valid_extension_to_data_path(
                        to_file, '.txt')
                    room_manager.print_text_to_file(to_file, text)
                    print('Successfully printed to {}'.format(to_file))
                    return to_file
                else:
                    print(text)
                    return ('Successfully printed allocations to screen')
        else:
            print('There are currently no rooms in Dojo.')
            return('There are currently no rooms in Dojo.')

    def print_unallocated(self, to_file=None):
        # prints people who are unallocated either to the stdout or a file
        if self.people:
            office_unallocated = person_manager.unallocated_list(
                self.people)[0]
            living_space_unallocated = person_manager.unallocated_list(
                self.people)[1]
            unallocated_office_text = self.format_text_persons_details(
                office_unallocated, 'office space')
            unallocated_living_space_text = self.format_text_persons_details(
                living_space_unallocated, 'living space')
            if not (unallocated_office_text or unallocated_living_space_text):
                print('No unallocated person in the System')
                return None
            if to_file:
                to_file = self.append_valid_extension_to_data_path(
                    to_file, '.txt')
                room_manager.print_text_to_file(
                    to_file, unallocated_office_text)
                room_manager.print_text_to_file(
                    to_file, unallocated_living_space_text)
                print(
                    'Successefully printed unallocated person(s) to {}'.format(
                        to_file))
                return to_file
            else:
                print(unallocated_office_text)
                print(unallocated_living_space_text)
                return 'Printed Allocation'
        else:
            print('Dojo currently has no person(s) yet!')
            return 'No person in the System Yet!'

    def people_id(self):
        # This allows user to easily check for a person's id.
        if self.people:
            print('ID          PERSON-DETAILS')
            for index, person in enumerate(self.people):
                print('{0}     {1}'.format(
                    index + 1, person.pname))
        else:
            print('No person added yet!!!')

    def reallocate_person(self, person_id, room_name):
        try:
            person = self.people[person_id - 1]
            new_room = [room for room in self.all_rooms
                        if room.name and room.name == room_name.upper()]
            new_room = new_room[0]
            if new_room.room_type == 'office':
                person_room = person.office
            else:
                person_room = person.living_space
            if person_room:
                current_room = room_manager.get_room_with_a_room_name(
                    person_room, self.all_rooms)
            else:
                current_room = None
            if (person.office == room_name.upper()) or ((
                    person.role == 'fellow') and
                    person.living_space == room_name.upper()):
                print('You cannot reallocate person to current room.')
                return 'You cannot reallocate person to current room.'
            else:
                room_manager.check_room_size(new_room)
                room_manager.check_person_can_be_in_room(new_room, person)
                room_manager.delete_person_from_room(current_room, person)
                room_manager.add_person_to_room(new_room, person)
                person_manager.assign_person_room_name(new_room, person)
                print('{0} has been reallocated to the {1} {2}'.format(
                    person.fname.title(), new_room.room_type,
                    new_room.name.upper()))
        except ValueError:
            print('Room is full, cannot reallocate {}'.format(
                person.fname.title()))
            return ('Room is full, cannot reallocate {}'.format(
                person.fname.title()))
        except TypeError:
            print('Person cannot be reallocated the room')
            return 'Person cannot be reallocated to the room'
        except IndexError:
            print('Id/Room_Name not found!')
            return('Id/Room_Name not found!')

    def load_people(self, text_file):
        # check to see if it is a valid text file, if not add the extension
        try:
            text_file = self.append_valid_extension_to_data_path(
                text_file, '.txt')
            with open(text_file, 'r') as load_people_source:
                for line in load_people_source.readlines():
                    values = line.split()
                    if len(values) == 3:
                        self.add_person(values[0], values[1], values[2])
                    elif len(values) == 4:
                        self.add_person(values[0],
                                        values[1], values[2], values[3])
                    else:
                        raise ValueError
        except FileNotFoundError:
            print('unable to locate file in {}'.format(self.DATA_DIR))
        except ValueError:
            print(' invalid format')

    def save_state(self, db_name='dojo.db'):
        # check if it is a valid extension else add the extension.
        db_name = self.append_valid_extension_to_data_path(db_name, '.db')
        if self.all_rooms or self.people:
            if db_name == self.DATA_DIR + 'dojo.db':
                print(
                    'Existing Data on default database dojo will be wiped.')
            app_session_data = (self.all_rooms, self.people)
            app_session_pickle = sqlite3.Binary(pickle.dumps(app_session_data))
            db = DojoDb(db_name)
            db.create_tables()
            db.save_data(app_session_pickle)
            return 'data persisted'

        else:
            print('Session has no data to persist to the database.')
            return ('Session not persisted, No data in app_session')

    def load_state(self, db_name):
        # check extension if not create it.
        db_name = self.append_valid_extension_to_data_path(db_name, '.db')
        try:
            db = DojoDb(db_name)
            app_session_pickle = db.get_data()
            loaded_app_session_data = pickle.loads(app_session_pickle)
            self.all_rooms = loaded_app_session_data[0]
            self.people = loaded_app_session_data[1]
            print('successful')
        except TypeError:
            print('Does not exist')
            return ('Bad Database given')
        except:
            print('Invalid db')
            return('Bad Database given')

    # These are helper methods used in other dojo methods.
    # HELPER METHODS
    def append_extension(self, data_file, extension):
        if data_file.endswith(extension):
            return data_file
        else:
            data_file += extension
            return data_file

    def check_or_make_data_dir_path(self):
        if os.path.exists(self.DATA_DIR):
            return self.DATA_DIR
        else:
            os.mkdir(self.DATA_DIR)
            return self.DATA_DIR

    def append_valid_extension_to_data_path(self, data_file, extension):
        data_file = self.append_extension(data_file, extension)
        self.DATA_DIR = self.check_or_make_data_dir_path()
        data_file = self.DATA_DIR + data_file
        return data_file

    def format_text_persons_details(self, people_list, room_type):
        person_text = ''
        for index, person in enumerate(people_list):
            person_data = '{0} {1}\n'.format(person.id, person.pname)
            person_text += person_data

        text = '(ID) UNALLOCATED LIST {0}\n {1}'.format(room_type.upper(),
                                                        person_text)

        if person_text:
            return text
        else:
            return None

    def delete_person_from_room(self, person, room):
        room.occupants.remove(person)

    def check_room_size(self, room):
        if len(room.occupants) < room.max_size:
            return True
        else:
            return False


dojo = Dojo()
dojo.add_person('ladi', 'adeniran', 'fellow')
dojo.create_room('office', ['Blue'])
dojo.reallocate_person(1, 'jdjd')
dojo.print_allocations()
