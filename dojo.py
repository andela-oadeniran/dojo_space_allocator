#!/usr/bin/env python

# import modules. sys, os, models and db modules to the main application.
import os
from os.path import expanduser
# import random
import sqlite3
import pickle
import termcolor
import sys
from termcolor import cprint
# from context import LivingSpace
# from context import Office
# from context import Room
from context import RoomManager
from context import PersonManager

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
        # The class calls on the room_manager methods to create a rooms.
        try:
            room_manager.check_valid_room_type(room_type)
            room_class = room_manager.return_living_office_class(room_type)
            for room_name in room_names:
                room_manager.check_room_name(room_name)
                if not room_manager.check_room_name_uniqueness(room_name,
                                                               self.all_rooms):

                    room = room_class(room_name)
                    room_manager.add_room_to_session(room, self.all_rooms)
                    print('added room {0} {1}'.format(
                        room_type, room_name.upper()))
                else:
                    print('Not unique')
        except TypeError:
            print('Invalid room type')
        except ValueError:
            print('Room name cannot be an empty string')

    def add_person(self, fname, lname, role, wants_accommodation='n'):
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
                'living', self.all_rooms)

            if available_office:
                room_manager.add_person_to_room(available_office, person)
                person_manager.assign_person_room_name(
                    available_office, person)
                print('added person to office')
            else:
                print('no offices')
            if ((person.role == 'fellow') and
                    person.wants_accommodation in ('y', 'Y')):
                if available_living_space:
                    room_manager.add_person_to_room(
                        available_living_space, person)
                    person_manager.assign_person_room_name(
                        available_living_space, person)
                    print('added person to living space')
                else:
                    print('no living spaces')
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
            else:
                print('No occupants')
        else:
            print('{} not a room in Dojo'.format(room_name.upper()))

    def print_allocations(self, to_file=None):
        # print_allocations take akey word argument to_file and defaults to 'n'
        # This should be passed when user justs wants to print to stdout and
        if self.all_rooms:
            for room in self.all_rooms:
                occupants = room_manager.string_room_occupants(room)
                if occupants:
                    text = '{0} {1}\n{2}\n{3}'.format(room.name,
                                                      room.room_type,
                                                      '-' * 30, occupants)
                else:
                    text = '{0} {1}\n{2}\n{0} has no occupants'.format(
                        room.name, room.room_type, '-' * 30)
                if to_file:
                    to_file = self.append_valid_extension_to_data_path(
                        to_file, '.txt')
                    room_manager.print_text_to_file(to_file, text)
                    print('Successfully printed to {}'.format(to_file))
                else:
                    print(text)
        else:
            print('There are currently no rooms in Dojo')

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
                print('No unallocated person')
                break
            if to_file:
                to_file = self.append_valid_extension_to_data_path(
                    to_file, '.txt')
                room_manager.print_text_to_file(
                    to_file, unallocated_office_text)
                room_manager.print_text_to_file(
                    to_file, unallocated_living_space_text)
            else:
                print(unallocated_office_text)
                print(unallocated_living_space_text)

        else:
            print('No person here')

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
        person = self.people[person_id - 1]
        room = [room for room in self.all_rooms
                if room.name and room.name == room_name.upper()]
        if room and person:
            room = room[0]
            try:
                if (person.office == room_name.upper()) or (
                        person.living_space == room_name.upper()):
                    print('cannot allocate to present room')
                else:
                    room_manager.check_room_size(room)
                    room_manager.check_person_can_be_in_room(room, person)
                    room_manager.delete_person_from_current_room(person)
                    room_manager.add_person_to_room(room, person)
                    person_manager.assign_person_room_name(room, person)
            except ValueError:
                print('Room is full')
            except TypeError:
                print('person cannot be allocated the room')

    def load_people(self, text_file):
        # check to see if it is a valid text file, if not add the extension
        # you don't want your users to always type the .txt everytime!!!
        if not text_file.endswith('.txt'):
            text_file += '.txt'
        # check if .dojo_data directory exists on the home folder
        if os.path.exists(self.data_dir):
            text_file = self.data_dir + text_file
            # check if the text file exists
            if os.path.isfile(text_file):
                with open(text_file, 'r') as load_people_source:
                    for line in load_people_source.readlines():
                        values = line.split()
                        if len(values) == 3:
                            self.add_person(values[0], values[1], values[2])
                        elif len(values) == 4:
                            self.add_person(values[0], values[1], values[2], values[3])
                        else:
                            cprint('Text in {} not properly formatted, check the documentation for format.'.format(text_file), 'magenta')
                    load_people_source.close()
            else:
                cprint('file doesn\'t exist in the ~/.dojo_data directory!!!', 'red')
        else:
            cprint('It seems you don\'t have a ~/.dojo_data folder!!! Create the directory and add a text file with the specified format', 'red')

    def save_state(self, db_name='dojo.db'):
        # check if it is a valid extension else add the extension. 
        if not db_name.endswith('.db'):
            db_name =  db_name + '.db'
        # check if path exists else create the path
        if os.path.exists(self.data_dir):
            db_name = self.data_dir  + db_name
        else:
            os.mkdir(self.home + '/.dojo_data/')
            self.data_dir = self.home + '/.dojo_data/'
            print(self.data_dir)
            db_name = self.data_dir + db_name
        # you don't want to save an empty session!!!
        if self.all_rooms or self.people:
            if db_name == self.data_dir + 'dojo.db':
                print ('Existing Data on default database dojo will be wiped off.')
            app_session_data = (self.app_session,self.all_rooms, self.people)
            app_session_pickle = sqlite3.Binary(pickle.dumps(app_session_data))
            db = DojoDb(db_name)
            db.create_tables()
            db.save_data(app_session_pickle)
            return 'data persisted'

        else:
            cprint('Session has no data to persist to the database.', 'magenta')
            return ('Session not persisted, No data in app_session')

    def load_state(self, db_name):
        # check extension if not create it.
        if not db_name.endswith('.db'):
            db_name += '.db'
            db_name = self.data_dir + db_name
        else:
            db_name = self.data_dir + db_name
        # check for validity of the path and the database itself
        if (os.path.isfile(db_name)):
            db = DojoDb(db_name)
            app_session_pickle = db.get_data()
            # check if it returns a valid session else print and return error message
            if app_session_pickle:
                loaded_app_session_data = pickle.loads(app_session_pickle)
                self.app_session = loaded_app_session_data[0]
                self.all_rooms = loaded_app_session_data[1]
                self.people = loaded_app_session_data[2]
                self.people_keys = [key for key in self.app_session['person'].keys()]
                cprint('state loaded from {}'.format(db_name), 'green')
            else:
                cprint ('The database is invalid and does not contain'
                ' data from the Applications\'s saved state.', 'red')
                return 'Bad Database given'
        else:
            cprint('Not a valid database check home/.dojo_data for the available databases', 'red')

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
            person_data = '{0} {1}\n '.format(person.id, person.pname)
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
dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
dojo.create_room('office', ['orion'])
dojo.create_room('living', ['blue'])

# dojo.add_person('ladi', 'adeniran', 'fellow')
# dojo.add_person('ladi', 'adeniran', 'fellow')
dojo.people_id()
dojo.print_unallocated('pop')



