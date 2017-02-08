#!/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    app create_room <room_type> <room_name> ...
    app add_room <person_name> <FELLOW/STAFF> [wants_accommodation]
    app [-i | --interactive]
    app
    app (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

#import modules
import os, sys
modelsdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir + '/dojo_space_allocator/models'))
sys.path.append(modelsdir)

from person import Person
from room import Room


import cmd
from docopt import docopt, DocoptExit

#define functions for docopt commands
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
        """Usage: create_room <room_type> <room_name>"""

        print(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <FELLOW/STAFF>
        [wants_accommodation]
        """

        print(arg)

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