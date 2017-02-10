#!/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    app create_room <room_type> <room_names> ...
    app add_room <fname> <lname> <person_type> [wants_accommodation]
    app [-i | --interactive]
    app
    app (-h | --help | --version)
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
from models.office import Office
from models.living import LivingSpace
from models.staff import Staff
from models.fellow import Fellow


import cmd
from docopt import docopt, DocoptExit



# The Dojo class contains the application logic and direct interaction
#with commands
#
class Dojo():
	"""The class serves as the project's controller"""
	def __init__(self):
		#create class variables
		db = Db()


	#methods that interact with Room, Office and LivingSpace classes
	def create_room(self, room_type, room_names):
		# parse this and make an instance of room for each case
		# check to see whether room type is valid
		valid = ['office', 'living']
		if (room_type.lower() == valid[0]):
			for room_name in room_names:
				# call the create_office function
				create_office(room_name)

		elif (room_type.lower()== valid[1]):
			for room_name in room_names:
				#call appropriate function
				create_living_space(room_name)
		else:
			raise ValueError('Not a valid room_type')

	#methods interacting with the Person, Fellow and Staff classes
	def add_person(self, fname, lname, )


# functions interacting with Room, Office and LivingSpace classes

def create_office(office_name):
	office_name = Office(office_name)

	# room_state['office'].append(self.office_name.room_name)
	# print("An office called "+ room_state['office'][0]+(" has been successfully created"))

def create_living_space(self, living_name):
	living_name = LivingSpace(living_name)






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
        except ValueError:
            print('Not a valid room_type')
        except:
            print('Not a valid usage')

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <fname> <lname> <person_type>
        [<wants_accommodation>]
        """
        try:
            Dojo().add_person(arg.get('<fname>'), arg.get('<lname>'), arg.get('<person_type>'), arg.get('<wants_accommodation>')  )
            print('end...')
        except ValueError:
            print ('Not a valid person_type. person_type can only be Fellow or Staff')
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
