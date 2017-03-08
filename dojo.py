#!/usr/bin/env python

# import modules. sys, os, models and db modules to the main application.
import os
from os.path import expanduser
import sys
import random
import sqlite3
import pickle
import termcolor
from termcolor import cprint

dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './db'))
modelsdir = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 './models'))

sys.path.append(dbdir)
sys.path.append(modelsdir)

from db.dojodb import DojoDb
from models.office import Office
from models.living import LivingSpace
from models.staff import Staff
from models.fellow import Fellow


class Dojo(object):
    """ The Dojo class Docstring
    People's names might not be unque but the ids here are.
    Room names are unique and are used as the room identifier
    """
    # instance variables and structures to hold app data
    def __init__(self):
        self.app_session = {'room': {}, 'person': {}}
        self.all_rooms = []
        self.people = []
        self.people_keys = []
        self.home = expanduser('~')
        self.data_dir = self.home + '/.dojo_data/'

    def create_room(self, purpose, room_names):
        # check if the purpose is either living or an office
        # and also check for uniqueness.
        if purpose.lower() in ('office', 'living'):
            # if room purpose given is office
            if purpose.lower() == 'office':
                for room_name in room_names:
                    if (room_name.upper() in self.app_session['room'].keys()):
                        cprint('{} already exists. '
                            'Use a different name'.format(room_name.upper()), 'red')
                    else:
                        room_key = room_name.upper()
                        # create an Office class instance of each argument supplied
                        room = Office(room_key)
                        # append the room to app session and print appropriate messages
                        self.append_room_to_session_data(room_key ,room)
                        cprint('An Office called {0} ' 
                            'has been successfully created!'.
                            format(room_key), 'green')
            else:
                for room_name in room_names:
                    # each room name is unique. print appropriate error message
                    if (room_name.upper() in self.app_session['room'].keys()):
                        cprint('Room name already exists,'
                            ' Use a different name', 'red' )
                    else:
                        room_key = room_name.upper()
                        room = LivingSpace(room_key)
                        self.append_room_to_session_data(room_key, room)
                        cprint('A Living Space called {} '
                            'has been successfully created!'.format(
                                room_key), 'green')
        else:
            cprint('The Room type {} is invalid, '
                'A room in Dojo can either be an ' 
                'office or a living Space.'.format(purpose), 'red')

    def add_person(self, fname, lname, role, wants_accommodation = 'n'):
        # check role of the person supplied must either be a staff or a fellow
        if role.lower() in ('fellow', 'staff'):
            if role.lower() == 'fellow':
                # create fellow from class Fellow
                fellow = Fellow(fname, lname, wants_accommodation)
                # check a random available office space
                available_office = self.get_available_room('office')
                if available_office:
                    self.allocate_person_to_room(fellow, available_office)
                if wants_accommodation in ('y', 'Y'):
                    # if a fellow wants accommodation check for available rooms and return it.
                    available_living = self.get_available_room('living')
                    if available_living:
                        self.allocate_person_to_room(fellow, available_living)
                # append person to session with
                self.append_person_to_session_data(fellow)
                # print appropriate messages when the fellow has or not an office
                # also if the fellow wants accommodation, if he has or not.
                cprint('Fellow {0} {1} has been successfully added.'.format(
                    fname.title(), lname.title()), 'green')
                if fellow.office:
                    cprint('{0} has been allocated the Office {1}'.
                        format(fellow.fname.title(), fellow.office), 'green')
                else:
                    cprint('There are currently no vacant office Spaces in Dojo.'
                        ' Create offices and reallocate the Fellow.', 'magenta')
                if wants_accommodation in ('y', 'Y'):
                    if fellow.living_space:
                        cprint('{0} has been allocated the Living space {1}'.
                            format(fellow.fname.title(), fellow.living_space), 'green')
                    else:
                        cprint('There are currently no vacant living Spaces in Dojo, Create'
                            ' a living Space and reallocate the Fellow to the Room.', 'magenta')
            else:
                # make an instance of the Staff class
                staff = Staff(fname, lname)
                available_office = self.get_available_room('office')
                if available_office:
                    self.allocate_person_to_room(staff, available_office)
                self.append_person_to_session_data(staff)
                cprint('Staff {0} {1} has been successfully added.'.
                    format(fname.title(), lname.title()), 'green')
                if staff.office:
                    cprint('{0} has been allocated the Office {1}'.
                        format(staff.fname.title(), staff.office), 'green')
                else:
                    cprint('There are currently no vacant office spaces in Dojo.'
                        ' Create offices and reallocate the Staff.', 'magenta')
        else:
            cprint('You can only add fellows and staff!!!', 'red')

    def print_room(self, room_name):
        # check if room exists in dojo
        if (self.all_rooms):
            room_key = room_name.upper()
            # check if the room name exists in dojo
            if room_key in self.app_session['room'].keys():
                occupants=  self.app_session['room'][room_key].occupants
                # check to see if the room has occupants
                if occupants:
                    occupants = [occupant.pname for occupant in occupants]
                    cprint ('ROOM ({0}) PURPOSE ({1})'.
                        format( self.app_session['room'][room_key].name,self.app_session['room'][room_key].purpose.upper()), 'green')
                    cprint(' , '.join(occupants), 'green')
                    return ', '.join(occupants)
                # if the room has o occupants print and return this
                else:
                    cprint ('{0} currently has no occupant(s)!'.
                            format(room_key), 'magenta')
                    return ('{} currently has no occupant(s)'.format(room_key))
            else:
                cprint('Room doesn\'t exist in Dojo!!!', 'red')
                return 'Room name not in session.'
        else:
            cprint('There are currently no rooms in Dojo.', 'magenta')
            return 'No rooms in Dojo.'

    def print_allocations(self , to_file = 'n'):
        # print_allocations take akey word argument to_file and defaults to 'n'
        # This should be passed when user justs wants to print to sys stdout and 
        # not have it stored.
        if (self.all_rooms):
            for room in self.all_rooms:
                # check to see if room contains occupants
                if (room.occupants):
                    members = ', '.join(
                        str(person).title() for person in room.occupants)
                    self.print_allocations_func(room, to_file,members)
        
                else:
                    self.print_allocations_func(room, to_file)
            # feedback for successful print to a text file
            if not to_file.lower() == 'n':
                if not to_file.endswith('.txt'):
                    to_file += '.txt'
                    file_path = self.data_dir + to_file
                else:
                    file_path = self.data_dir + to_file
                cprint('Successfully written Allocations to {0}.\n'.
                       format(file_path), 'green')
                return file_path
            else:  
                return 'Successfully printed allocations to screen'
                

        else:
            cprint('There are currently no rooms in Dojo', 'magenta')
            return ('There are currently no rooms in Dojo.')

    def print_unallocated(self, to_file='n'):
        to_file_living = to_file
        if (self.people):
            # make a list of fellows and staff with no offices
            # make a list of fellows that want accommodation but have none
            no_office_allocated_list = [person for person in self.people if not person.office]
            list_of_fellows = [person for person in self.people if person.role =='fellow']
            no_living_space_allocated_list = [person for person in list_of_fellows if person.wants_accommodation.lower()=='y' and not person.living_space]
            if (no_office_allocated_list) or (no_living_space_allocated_list):
                cprint('ID       Person DETAILS', 'green')
                if no_office_allocated_list:
                    for person in no_office_allocated_list:
                        self.print_unallocated_func(person,'office', to_file)
                    if to_file not in ('N', 'n'):
                        if not to_file.endswith('.txt'):
                            to_file+= '.txt'
                            file_path = self.data_dir + to_file
                        else:
                            file_path =self.data_dir + to_file
                        cprint('Successfully written person(s) that need office spaces {}'.format(file_path), 'green')

                if no_living_space_allocated_list:
                    for person in no_living_space_allocated_list:
                        self.print_unallocated_func(person, 'living', to_file)
                    if to_file not in ('N', 'n'):
                        if not to_file.endswith('.txt'):
                            to_file+= '.txt'
                            file_path = self.data_dir + to_file
                        else:
                            file_path =self.data_dir + to_file
                        cprint('Successfully written person(s) that need living spaces {}'.format(file_path), 'green')
                return 'Printed Allocation'
            else:
                cprint('There are no unallocated people', 'magenta')
                return None
        else:
            cprint('No person in the System Yet!', 'red')
            return 'No person in the System Yet!'

    def people_id(self):
        # This allows user to easily check for a person's id.
        if self.people:
            cprint('PERSON-ID          PERSON-DETAILS', 'green')
            for index, person_key in enumerate(self.people_keys):
                cprint('{0}     {1}'.format(person_key, self.people[index].pname))
        else:
            cprint('No person added yet!!!', 'red')

    def reallocate_person(self, person_id, room_name):
        if (person_id in self.people_keys) and (room_name.upper() in self.app_session['room'].keys()):
            if (self.app_session['person'][person_id].office != room_name.upper()):
                room_key = room_name.upper()
                room = self.app_session['room'][room_key]
                person = self.app_session['person'][person_id]
                # check to see if the intended allocation is full
                if (self.check_room_size(room)):
                    # check to see if the room-provided's purpose and separate
                    # the function enters the condition office for staff and fellows
                    if room.purpose == 'office':
                        if person.office:
                            # person previously has an office, delete  person from the office.
                            self.delete_person_from_room(
                                person, self.app_session['room'][person.office])
                            # add person to the new allocated office
                            person.office = self.add_person_to_room(person, room)
                            cprint('{0} has been allocated the office {1}'.format(
                                person.fname, room.name), 'green')
                        else:
                            # if a person does not have an office go ahead and allocate an office to the person.
                            person.office = self.add_person_to_room(person, room)
                            cprint('{0} has been allocated the office {1}'.format(
                                person.fname, room.name), 'green')
                    else:
                        # condition that seives for fellows that want a living space
                        if person.role == 'fellow':
                            # check if fellow wants a living space.
                            if person.wants_accommodation in ('y', 'Y'):
                                if (self.app_session['person'][person_id].living_space != room_name.upper()):
                                    if person.living_space:
                                        # if a person has a living space prior delete person from the living space and allocate person to the new room
                                        self.delete_person_from_room(
                                            person, self.app_session['room'][person.living_space])
                                        person.living_space = self.add_person_to_room(
                                            person, room)
                                        cprint(
                                            '{0} has been allocated the living space {1}'.
                                            format(person.fname, room.name), 'green')
                                    else:
                                        # If person doesn't have a living space go ahead and give the person a space.
                                        person.living_space = self.add_person_to_room(
                                            person, room)
                                        cprint(
                                            '{0} has been allocated the living space {1}'.
                                            format(person.pname, room.name), 'green')
                                else:
                                    cprint("You cannot reallocate a person to current room", 'red')
                                    return 'You cannot reallocate person to current room'

                        else:
                            cprint('You cannot add Staff {}, to a living Space.'.format(person.pname), 'red')
                else:
                    cprint('You cannot Reallocate to a full Room', 'red')
            else:
                cprint("You cannot reallocate a person to current room", 'red')
                return 'You cannot reallocate person to current room'

        else:
            cprint('Invalid Person ID or Room Name', 'red')
            return 'Invalid Person Identifier or Room'

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

    #These are helper methods used in other dojo methods.
    def add_person_to_room(self,person, room):
        room.occupants.append(person)
        return room.name


    def delete_person_from_room(self, person, room):
        room.occupants.remove(person)


    def check_room_size(self, room):
        if len(room.occupants) < room.max_size:
            return True
        else:
            return False


    def get_available_room(self, purpose):
        available_rooms = [room for room in self.all_rooms if room.purpose == purpose and len(room.occupants) < room.max_size]
        if available_rooms:
            room = random.choice(available_rooms)
            return room
        return None

    def allocate_person_to_room(self, person, room):
        self.add_person_to_room(person, room)
        if room.purpose == "office":
            person.office = room.name
        elif room.purpose == "living":
            person.living_space = room.name

    def append_room_to_session_data(self, room_key, room_object):
        self.all_rooms.append(room_object)
        self.app_session['room'][room_key] = room_object

    def append_person_to_session_data(self,person_object):
        # function to help put a person to apllication session
        self.people.append(person_object)
        person_key = len(self.people)
        person_object.id = person_key
        self.app_session['person'][person_key] = person_object
        self.people_keys.append(person_key)

    def print_unallocated_func(self, person_object, room_purpose_needed, print_to_file):
        text = '({0}) {1} ({2}) space needed\n'.format(person_object.id, person_object.pname, room_purpose_needed)
        # check if the user wants to output on the screen or have it written in a text file
        if print_to_file in ('n', 'N'):
            cprint(text, 'magenta')
        else:
            if not print_to_file.endswith('.txt'):
                print_to_file += '.txt'
            if os.path.exists(self.data_dir):
                print_to_file = self.data_dir + print_to_file
            else:
                # create the directory if not exist.
                os.mkdir(self.data_dir)
                print_to_file = self.data_dir + print_to_file
            with open(print_to_file, 'a') as unallocated_file:
                unallocated_file.write(text)
                unallocated_file.close()

    def print_allocations_func(self,room,print_to_file, room_occupants=None):
        # if a room has occupants text is formed with the members list.
        dash_lines = '-'*60
        if room_occupants:  
            text = ('{0}\n{1}\n{2}\n'.format(room.name,dash_lines, room_occupants))
            if print_to_file.lower() == 'n':
                cprint(text, 'green')
            else:
                # check to see the print to file details
                if not print_to_file.endswith('.txt'):
                    print_to_file = print_to_file + '.txt'
                if os.path.exists(self.data_dir):
                    print_to_file = self.data_dir + print_to_file
                else:
                    os.mkdir(self.data_dir)
                    print_to_file = self.data_dir + print_to_file
                with open(print_to_file, 'a') as allocations_file:
                    allocations_file.write(text)
                    allocations_file.close()     
        else:
            # rooms with no occupants
            text = ('{0}\n{1}\n{0} has no occupants yet\n'.format(room.name, dash_lines))
            if print_to_file.lower()=='n':
                cprint(text, 'green')
            else:
                # check the details and print to the write file
                if not print_to_file.endswith('.txt'):
                    print_to_file = print_to_file + '.txt'
                if os.path.exists(self.data_dir):
                    print_to_file = self.data_dir + print_to_file
                else:
                    os.mkdir(self.data_dir)
                    print_to_file = self.data_dir + print_to_file
                with open(print_to_file, 'a') as allocations_file:
                    allocations_file.write(text)
                    allocations_file.close()







