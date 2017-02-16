

#import modules and the models and db directory to the app's entry.

import os, sys
dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './db'))
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), './models'))

sys.path.append(dbdir)
sys.path.append(modelsdir)

from db.db import Db
from models.room import Room
from models.office import Office
from models.living import LivingSpace
from models.person import Person
from models.staff import Staff
from models.fellow import Fellow







# The Dojo class contains the application logic and direct interaction
class Dojo():
    """ The Dojo class Docstring"""
    app_session = {'room':[], 'person':[]}

    def __init__(self):
        pass

    def create_room(self, room_type, room_names):
        valid_rooms = ('office','living')
        rooms = []
        if room_type.lower()== valid_rooms[0]:
            for index, room_name in enumerate(room_names):
                #room_data = {}
                if not (room_exists(room_name, 'room')):
                    room = Room('office', room_name)
                    # key_name = room_name
                    # room_name = create_room(room_name, 'office')
                    # print(room_name.room_name)
                    # room_data['room_name'] = room_name.room_name
                    # room_data['room_type'] = room_name.room_type
                    # room_data['room_occupants'] = room_name.room_occupants
                    # room_data['max_occupants'] = room_name.maxoccupant
                    # room_data['room_size'] = room_name.add_room_size()
                    Dojo.app_session['room'].append(room)
                    print(Dojo.app_session['room'])
                    print("office room was created")
                    rooms.append(room)
                else:
                    print('room already exists can you name it something else')

        elif room_type.lower() == valid_rooms[1]:
            for index, room_name in enumerate(room_names):
                room_data = {}
                if not (room_exists(room_name, 'room')):
                    room = Room('living', room_name)
                    # key_name = room_name
                    # room_name = create_room(room_name, 'living')
                    # print(room_name.room_name)
                    # room_data['room_name'] = room_name.room_name
                    # room_data['room_type'] = room_name.room_type
                    # room_data['room_occupants'] = room_name.room_occupants
                    # room_data['max_occupants'] = room_name.maxoccupant
                    # room_data['room_size'] = room_name.add_room_size()
                    Dojo.app_session['room'].append(room)
                    rooms.append(room)
                    print(Dojo.app_session['room'])
                    print("living room was created")
                else:
                    print('room already exists can you name it something else')


        else:
            raise TypeError
        return rooms

    def add_person(self, fname, lname, person_type, wants_accommodation='n'):
        valid_persons = ['fellow', 'staff']
        if (person_type.lower() == valid_persons[0]) and (wants_accommodation.lower() == 'y' or wants_accommodation== 'yes'):
            person_name = '{0} {1}'.format(fname, lname)
            create_person(person_name, 'fellow', 'y')

            # add_person_to_room(person_name, 'fellow', 'y')


        elif person_type.lower()==valid_persons[0]:
            fellow_name = '{0} {1}'.format(fname, lname)
            create_person(fellow_name, valid_persons[0], 'n')
            # add_person_to_room(person_name, 'fellow', 'n')


        elif person_type.lower() == valid_persons[1]:
            person_data = {}
            person_name = '{0} {1}'.format(fname, lname)
            if not(check_unique_name(person_name, 'person')):
                key_name = person_name
                person_name = create_person(person_name, 'staff', 'n')
                person_data['person_name'] = person_name.person_name
                person_data['person_type'] = person_name.person_type
                # person_data['person_room'] = person_name.person_room
                #get room you want to add the person too from db / datastructure the details are stored
                # print(person_name)
                Dojo.app_session['person'].append(person_data)
                print(Dojo.app_session['person'])
                print("added staff")
                room_name = add_person_to_room(key_name, 'n')
                #
                #person_room = room_name.room_name
            else:
                print("name already exists")


        else:
            raise TypeError




#functions used by the methods in the dojo class
#
#       FUNCTION NAME                   FUNCTION USE
#
#
#
#



#function to check if a room name already exists
def room_exists(name, app_session_key):
    return any([room.room_name.lower() == name.lower() \
        for room in Dojo.app_session['room']])


    # app_session_room_or_person_name_arr = []
    # if app_session_key == 'room':
    #     for index, value in enumerate(Dojo.app_session['room']):
    #         app_session_room_or_person_name_arr.append(value['room_name'])
    #         if (name in app_session_room_or_person_name_arr):
    #             return True
    #         else:
    #             return False
    # else:
    #     for index, value in enumerate(Dojo.app_session['person']):
    #         app_session_room_or_person_name_arr.append(value['person_name'])
    #         if (name in app_session_room_or_person_name_arr):
    #             return True
    #         else:
    #             return False


#function to create an instance of the Office or LivingSpace class
def create_room(room_name, room_type):
    if room_type == 'office':
        room_name = Office(room_name)
        return room_name
    else:
        room_name = LivingSpace(room_name)
        return room_name

def create_person(person_name, person_type, wants_accommodation):

    if person_type == 'fellow' and wants_accommodation =='y':
        person_name = Fellow(person_name, 'y')
        print(" wants accommodation")

    elif person_type == 'fellow' and wants_accommodation=='n':
        person_name = Fellow(person_name)
        print(' doesn\'t want an accommodation and specified properly ')
    elif person_type == 'fellow' and wants_accommodation!='n':
        person_name = Fellow(person_name)
        print(' not added to living Space valid argument is "y" or "yes"')
    elif person_type == 'staff' and wants_accommodation=='n':
        # get instance of the staff class and pass the appropriate arguments to db/data_structure
        person_name = Staff(person_name)
        print("staff added with the appropriate argument for wants_accommodation")
        return person_name

    else:
        person_name = Staff(person_name)
        print("Living rooms are only available for fellows ")

#function to check whether a room is full
def check_room_full(room_name):
    #check how you are storing the names in the office and living classes
    return True

#add a person to a room_type (office or living)and increase
#the number of people there and check if it's
#less than (4 for living or 6 for offices)
#function to add a person to a room that is not full
def add_person_to_room(person_name, wants_accommodation):
    if wants_accommodation == 'n':
        print(Dojo.app_session['room'])
        #get an office that is not full and then append the person to the occupants
        #add to office to instance of office if not full
        #loop through the offices and add to one that is not full
        for index, value in enumerate(Dojo.app_session['room']):
            print(value)
            if(value['room_size'] < value['max_occupants']):
                value['room_occupants'].append(person_name)
                value['room_size'] += 1
                print(value['room_occupants'])
                print(value)
                break
            else:
                print("well i think we need more offices")
    else:
        pass






# Dojo().add_person('oladipupo', 'Adeniran', 'staff')












#define functions for docopt commands and cmd for interactiveness
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

