#!/usr/bin/env python

#import modules and the models and db directory to the app's entry.

import os, sys
dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './db'))
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './models'))

sys.path.append(dbdir)
sys.path.append(modelsdir)

# from db.db import Db
# from models.room import Room
from models.office import Office
from models.living import LivingSpace
# from models.person import Person
from models.staff import Staff
from models.fellow import Fellow







# The Dojo class contains the application logic and direct interaction
class Dojo():
    """ The Dojo class Docstring"""
    app_session = {'room':[], 'person':[]}
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
                    if ( room_name in Dojo.room_keys):
                        print ('Room name already exists. Use a different name')
                    else:
                        room_key = room_name
                        room_name = Office(room_name)
                        Dojo.all_rooms.append(room_name)
                        Dojo.app_session['room'].append({room_key: room_name})
                        Dojo.room_keys.append(room_key)
                        print(self.room_keys)
                        print("An Office called {0} has been successfully created!".format(room_key))
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
                        print("A Living Space called {0} has been successfully created!".format(room_key))
                        return room_name
        else:
            print ('Dojo contains Offices and Living Spaces ')

    def add_person(self, fname, lname, role, wants_accommodation='n'):
        self.people_keys = Dojo.people_keys
        if role.lower() in ('fellow', 'staff'):
            if role.lower() == 'fellow':
                # Improve on this and check with user before having duplicate names
                # 001,002 etc implement that
                person_name = "{0} {1}".format(fname, lname)
                fellow_name = person_name
                fellow_name = Fellow(fname, lname, wants_accommodation)

                Dojo.people.append(fellow_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'].append({person_key: fellow_name})
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)
                print('Fellow {0} has been successfully added.'.format(person_name))
                return fellow_name



            else:
                person_name = "{0} {1}".format(fname, lname)
                staff_name = person_name
                staff_name = Staff(fname, lname)

                Dojo.people.append(staff_name)
                person_key = len(Dojo.people)
                Dojo.app_session['person'].append({person_key: staff_name})
                Dojo.people_keys.append(person_key)
                # Dojo.app_session['person'].append(person_key)
                # print (Dojo.app_session['person'])
                # print (Dojo.people_keys)
                print('Staff {0} has been successfully added.'.format(person_name))
                return staff_name


        else:
            print('You can only add fellows and staff')
    def print_room(self, room_name):
        pass

    def print_allocations(self, to_file='n'):
        pass



    def reallocate_person(self, person_name, room_name):
        pass

    def load_people(self):
        pass

    def save_state(self):
        pass

    def load_state(self, db_sql):
        pass


# dojo = Dojo()
# dojo.add_person('ladi', 'Adeniran', 'staff')
# dojo.add_person('ladi', 'Adeniran', 'fellow')
# dojo.add_person('ladi', 'Adeniran', 'staff')

# dojo.create_room('living', ['Orange', 'Orange'])
# dojo.create_room('office', ['Orion', 'Dev', 'fly'])


#
#       FUNCTION NAME                   FUNCTION USE
#
#
#
#









