#!/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    dojo create_room <room_type> <room_names> ...
    dojo add_room (<fname> <lname> <FELLOW/STAFF> [<wants_accommodation>])
    dojo [-i | --interactive]
    dojo
    dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

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


import cmd
from docopt import docopt, DocoptExit



# The Dojo class contains the application logic and direct interaction
class Dojo():
    """ The Dojo class Docstring"""
    def __init__(self):
        pass

    def create_room(self, room_type, room_names):
        valid_rooms = ['office','living']
        if room_type.lower()== valid_rooms[0]:
            for index, room_name in enumerate(room_names):
                create_office(room_name)
        elif room_type.lower() == valid_rooms[1]:
            for index, room_name in enumerate(room_names):
                create_living_space(room_name)
        else:
            raise TypeError
    def add_person(self, fname, lname, person_type, wants_accommodation):
        valid_persons = ['fellow', 'staff']
        if (person_type.lower() == valid_persons[0]) and (wants_accommodation.lower() == 'y' or wants_accommodation== 'yes'):
            fellow_name = '{0} {1}'.format(fname, lname)
            create_person(fellow_name, 'fellow', 'y')
            # add_person_to_office(person_name)
            # add_person_to_living(person_name)


        elif person_type.lower()==valid_persons[0]:
            fellow_name = '{0} {1}'.format(fname, lname)
            create_person(fellow_name, valid_persons[0], wants_accommodation)
            # add_person_to_office(person_name)


        elif person_type.lower() == valid_persons[1]:
            person_name = '{0} {1}'.format(fname, lname)
            create_person(person_name, valid_persons[1], wants_accommodation)
            # add_person_to_office(person_name)
        else:
            raise TypeError



office_arr = []
living_arr = []
room_state = {'living':living_arr, 'office':office_arr}

def create_office(office_name):
	office_name = Office(office_name)

	# room_state['office'].append(self.office_name.room_name)
	# print("An office called "+ room_state['office'][0]+(" has been successfully created"))

def create_living_space(living_name):
	living_name = LivingSpace(living_name)

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
        person_name = Staff(person_name)
        print("staff added with the appropriate argument for wants_accommodation")

    else:
        person_name = Staff(person_name)
        print("Living rooms are only available for fellows ")







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


#for interactive shell define the class
class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'dojo>>>'
    file = None

    #use decorators to define the functions
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_names>..."""
        try:
            Dojo().create_room(arg.get('<room_type>'), arg.get('<room_names>'))
            print ('end ...')
        except TypeError:
            print ('Not a valid room type try "living or office".')
        except:
            print('Not a valid usage')

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person (<fname> <lname> <FELLOW/STAFF> [<wants_accommodation>])
        """
        try:
            if(arg.get('<wants_accommodation>')):
                Dojo().add_person(arg.get('<fname>'), arg.get('<lname>'), arg.get('<FELLOW/STAFF>'), arg.get('<wants_accommodation>','n')  )
                print('end valid wants_accommodation...')
            else:
                print (arg)
                Dojo().add_person(arg.get('<fname>'), arg.get('<lname>'), arg.get('<FELLOW/STAFF>'), 'n')
                print('end None for want_accommodation...')
        except TypeError:
            print ('<FELLOW/STAFF> type person can only be a Fellow or Staff')
        except:
            print('Not a valid usage')
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

#parse the argument
opt = docopt(__doc__, sys.argv[1:])

#allow the default for running the app to be interactive
if opt['Interactive'] or not(opt['Options:']):
    MyInteractive().cmdloop()

print(opt)
