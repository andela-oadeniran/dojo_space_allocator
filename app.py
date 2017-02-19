#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    app.py
    app.py create_room <room_type> <room_name>...
    app.py add_person <fname> <lname> <FELLOW/STAFF> [<wants_accommodation>]
    app.py print_room <room_name>
    app.py print_allocations [-o=<filename>]
    app.py print_unallocates [-o=<filename>]
    app.py people_id
    app.py reallocate_person <person_identifier> <new_room_name>
    app.py load_people
    app.py save_state [--db=<sqlite_database>]
    app.py load_state <sqlite_database>
    app.py (-i | --interactive)
    app.py (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'dojo>>>'
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>...
        """


    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <fname> <lname> <FELLOW/STAFF> [<wants_accommodation>]
        """
        pass
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>
        """
        pass

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o=<filename>]
Options:
    -o=<filename> Textfile [Default: rooms.txt]
        """
        pass
    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [-o=<filename>]
Options:
    -o=<filename> Textfile [Default: persons.txt]
        """
        pass
    @docopt_cmd
    def do_people_id (self, arg):
        """Usage: people_id
        """
    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>
        """
        pass
    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people
        """
        pass
    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=<sqlite_database>]
Options:
    --db=<sqlite_database> database [Default: app_session]
        """
        pass
    @docopt_cmd
    def do_load_state (self, arg):
        """Usage: load_state <sqlite_database>
        """
        pass


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:], version=1.0)

if not opt['--interactive'] or opt['--interactive']:
    MyInteractive().cmdloop()



print(opt)