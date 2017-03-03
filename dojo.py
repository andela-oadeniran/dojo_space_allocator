#!/usr/bin/env python

# import modules and the models and db directory to the app's entry.
import os
import sys
import random
import sqlite3
import pickle

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


# The Dojo class contains the application logic and direct interaction
class Dojo(object):
    """ The Dojo class Docstring
    People's names might not be unque but the ids here are.
    Room names are unique and are used as the room identifier
    """
    # Class instance Variable.
    app_session = {'room': {}, 'person': {}}
    all_rooms = []
    people = []
    people_keys = []

    def __init__(self):
        pass

    def create_room(self, purpose, room_names):
        # check if the purpose is either living or an office
        # and also check for uniqueness.
        self.app_session = Dojo.app_session
        self.all_rooms = Dojo.all_rooms
        self.people = Dojo.people
        self.people_keys = Dojo.people_keys
        if purpose.lower() in ('office', 'living'):
            if purpose.lower() == 'office':

                for room_name in room_names:
                    if (
                            room_name.upper() in Dojo.app_session['room'].keys()):
                        print(
                            'Room name already exists. Use a different name\n')
                    else:
                        room_key = room_name.upper()
                        room_name = Office(room_key)
                        append_room_to_session(room_key,room_name)
                        print(
                            "An Office called {0} has been successfully created!\n".
                            format(room_key.title()))
            else:
                for room_name in room_names:
                    if (room_name.upper() in Dojo.app_session['room'].keys()):
                        print("Room name already exists, Use a different name")
                    else:
                        room_key = room_name.upper()
                        room_name = LivingSpace(room_key)
                        append_room_to_session(room_key, room_name)
                        print(
                            "A Living Space called {0} has been successfully created!\n".format(
                                room_key.title())
                        )
        else:
            print(
                'The Room type is invalid, A dojo room can only be an Office or a Living Space.\n')

    def add_person(self, fname, lname, role, wants_accommodation='n'):
        if role.lower() in ('fellow', 'staff'):
            if role.lower() == 'fellow':
                fellow = Fellow(fname, lname, wants_accommodation)
                print('Fellow {0} {1} has been successfully added.'.format(
                    fname, lname))
                available_office = get_available_room('office')
                if available_office:
                    allocate_person_to_room(fellow, available_office)
                else:
                    print('There are currently no Office Spaces in Dojo.'
                        ' Create Offices and reallocate the Fellow. \n')
                if wants_accommodation in ('y', 'Y'):
                    available_living = get_available_room('living')
                    if available_living:
                        allocate_person_to_room(fellow, available_living)
                    else:
                        print('There are currently no Living Spaces in Dojo, Create'
                            'a living Space and reallocate the Fellow to the Room.')
                append_person_to_session(fellow)

            else:
                person_name = "{0} {1}".format(fname, lname)
                staff = Staff(fname, lname)
                print('Staff {0} has been successfully added.'.format(
                    person_name))
                available_office = get_available_room('office')
                if available_office:
                    allocate_person_to_room(staff, available_office)
                else:
                    print('There are currently no Office Spaces in Dojo.'
                        ' Create Offices and reallocate the Staff member. \n')

                append_person_to_session(staff)
        else:
            print('You can only add fellows and staff\n')

    def print_room(self, room_name):
        if (Dojo.all_rooms):
            room_key = room_name.upper()
            if room_key in Dojo.app_session['room'].keys():
                occupants_object =  Dojo.app_session['room'][room_key].occupants
                if occupants_object:
                    occupants = [str(occupant).title() for occupant in occupants_object]
                    print(' , '.join(occupants))
                else:
                    print ('{0} currently has no Occupant!\n'.format(room_key.title()))
        else:
            print('There are currently no rooms in Dojo.\n')

    def print_allocations(self, to_file='n'):
        if (Dojo.all_rooms):
            for room in Dojo.all_rooms:
                if (room.occupants):
                    members = ', '.join(
                        str(person).title() for person in room.occupants)
                    text = '{0}\n---------------------------\n{1}\n'.format(room.name.title(), members)
                    if not (to_file.endswith('.txt')):
                        print(text)
                    else:
                        file = open(to_file, 'a')
                        file.write(text)
                        file.close()
                        print('Successfully written Allocations to {0}.\n'.
                              format(to_file))
                else:
                    text = '{0}\n----------------------\n{1} is empty.\n'.format(
                        room.name.upper(), room.name.title())
                    if not(to_file.endswith('.txt')):
                        print(text)
                    else:
                        file = open(to_file, 'a')
                        file.write(text)
                        file.close()
                        print('Successfully written Allocations to {0}.\n'.
                              format(to_file))

    def print_unallocated(self, to_file='n'):
        if (Dojo.people):
            for person in Dojo.people:
                if not (person.office):
                    if not (to_file.endswith('.txt')):
                        print(
                            '{1} {0} needs an Office.\n\n'.format(str(person).title(), person.role.upper()))
                    else:
                        text = ('{0} needs an Office.\n\n'.format(
                            str(person).title()))
                        file = open(to_file, 'a')
                        file.write(text)
                        file.close()

                if (person.role == 'fellow'):
                    if ((person.wants_accommodation == 'y') and (not person.living_space)):
                        if not (to_file.endswith('.txt')):
                            print(
                            'FELLOW {0} needs a Living Space.\n'.format(str(person).title()))
                        else:
                            text = ('{0} needs a Living Space.\n\n'.format(
                                str(person).title()))
                            file = open(to_file, 'a')
                            file.write(text)
                            file.close()
                            print('{0} needs a Living Space'.format(
                                str(person).upper()))
        else:
            print('No person allocated to Dojo rooms yet')

    def people_id(self):
        print('ID          PERSON              ROLE\n')
        for index, person_key in enumerate(Dojo.people_keys):
            print('{0}     {1}        {2}'.format(person_key, Dojo.people[index], Dojo.people[index].role.upper()))

    def reallocate_person(self, person_id, room_name):
        if (person_id in Dojo.people_keys) and (room_name.upper() in Dojo.room_keys):
            if (Dojo.app_session['person'][person_id].office != room_name.upper()) or (Dojo.app_session['person'][person_id].living_space == room_name.upper()):
                room_key = room_name.upper()
                room = Dojo.app_session['room'][room_key]
                person = Dojo.app_session['person'][person_id]
                if (check_room_size(room)):
                    if room.purpose == 'office':
                        if person.office:
                            delete_person_from_room(
                                person, Dojo.app_session['room'][person.office])
                            person.office = add_person_to_room(person, room)
                            print('{0} has been allocated the office {1}'.format(
                                person.fname, room.name))
                        else:
                            person.office = add_person_to_room(person, room)
                            print('{0} has been allocated the office {1}'.format(
                                person.fname, room.name))
                    else:
                        if person.role == 'fellow':
                            if person.wants_accommodation == 'y':
                                if person.living_space:
                                    delete_person_from_room(
                                        person, Dojo.app_session['room'][
                                            person.living_space])
                                    person.living_space = add_person_to_room(
                                        person, room)
                                    print(
                                        '{0} has been allocated\
                                        the living space {1}'.
                                        format(person.fname, room.name))
                                else:
                                    person.living_space = add_person_to_room(
                                        person, room)
                                    print(
                                        '{0} has been allocated\
                                        the living space {1}'.
                                        format(person.fname, room.name))
                        else:
                            print('You cannot add {}, a Staff to a living Space.'.
                                  format(person.fname))
                else:
                    print('You cannot Reallocate to a full Room')
            else:
                print("You cannot reallocate a person to his present room")

        else:
            print('Invalid Person Id or Room name')

    def load_people(self, text_file):
        if text_file.endswith('.txt'):
            file = open(text_file)

            for line in file.readlines():
                values = line.split()
                if len(values) == 3:
                    self.add_person(values[0], values[1], values[2])
                elif len(values) == 4:
                    self.add_person(values[0], values[1], values[2], values[3])
                else:
                    pass
            file.close()
        else:
            print('Invalid text file, can only load people from a text file')

    def save_state(self, db_name='dojo.db'):
        if Dojo.all_rooms or Dojo.people:
            # if Dojo.all_rooms and Dojo.people:

            app_session_data = (Dojo.app_session,Dojo.all_rooms, Dojo.people)
            app_session_pickle = sqlite3.Binary(pickle.dumps(app_session_data))
            db = DojoDb(db_name)
            db.create_tables()
            db.save_data(app_session_pickle)
        else:
            print('Session has no data to persist to the database.')

    def load_state(self, db_name):
        db = DojoDb(db_name)
        app_session_pickle = db.get_data()
        app_session_data = pickle.loads(app_session_pickle)
        app_session = app_session_data[0]
        all_rooms = app_session_data[1]
        people = app_session_data[2]
        people_keys = [key for key in app_session['person'].keys()]

        print(all_rooms)
        print(app_session)
        print(people)
        print(people_keys)



# Functions used in the Dojo Class

def add_person_to_room(person, room):
    room.occupants.append(person)
    return room.name

def delete_person_from_room(person, room):
    room.occupants.remove(person)

def check_room_size(room):
    if len(room.occupants) < room.max_size:
        return True
    else:
        return False

def get_available_room(purpose):
    rooms = Dojo.all_rooms
    available_rooms = []
    for room in rooms:
        if (room.purpose == purpose) and (len(room.occupants) < room.max_size):
            available_rooms.append(room)
    if available_rooms:
        room = random.choice(available_rooms)
        return room
    return None

def allocate_person_to_room(person, room):
    add_person_to_room(person, room)
    if room.purpose == "office":
        person.office = room.name
        print('{0} has been allocated the Office {1}\n'.
              format(person.fname, room.name))
    elif room.purpose == "living":
        person.living_space = room.name
        print('{0} has been allocated the Living space {1}\n'.
              format(person.fname, room.name))

def append_room_to_session(room_key, room):
    Dojo.all_rooms.append(room)
    Dojo.app_session['room'][room_key] = room


def append_person_to_session(person):
    Dojo.people.append(person)
    person_key = len(Dojo.people)
    # person.id = person_key
    Dojo.app_session['person'][person_key] = person
    Dojo.people_keys.append(person_key)



# dojo = Dojo()
# dojo.create_room('office', ['Red'])
# dojo.add_person('ladi', 'adeniran', 'fellow')
# dojo.add_person('ladipupo','Adeni', 'fellow')
# print(Dojo.app_session)
# dojo.save_state()
# dojo.load_state('dojo.db')

# dojo = Dojo()
# dojo.create_room('office', ['Blue'])
# dojo.save_state()
# dojo.create_room('office', ['Blue'])
# dojo.save_state()
# dojo.load_people('dojo.db')