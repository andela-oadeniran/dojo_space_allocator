#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    app.py
    app.py create_room <room_type> <room_names>...
    app.py add_person <fname> <lname> <FELLOW/STAFF> [<wants_accommodation>]
    app.py print_room <room_name>
    app.py print_allocations [(-o <filename>)]
    app.py print_unallocated [(-o <filename>)]
    app.py people_id
    app.py reallocate_person <person_identifier> <room_name>
    app.py load_people <filename>
    app.py save_state [(--db sqlite_database)]
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
from pyfiglet import Figlet
from termcolor import colored, cprint

from dojo import Dojo
dojo = Dojo()

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


class MyInteractive(cmd.Cmd):
    fig_font = Figlet(font='graffiti')
    welcome_text = fig_font.renderText('Dojo Space Allocator')
    welcome_text = colored(welcome_text, 'green') + colored('Type help to get commands', 'magenta')
    intro = welcome_text
    prompt = colored('dojo>>>', 'cyan')
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_names>...
        """
        room_purpose = arg.get('<room_type>')
        room_names = arg.get('<room_names>')
        dojo.create_room(room_purpose, room_names)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <fname> <lname> <FELLOW/STAFF> [<wants_accommodation>]
        """
        fname = arg.get('<fname>')
        lname = arg.get('<lname>')
        person_type = arg.get('<FELLOW/STAFF>')
        wants_accommodation = arg.get('<wants_accommodation>')
        if fname.isalpha() and lname.isalpha():
            if person_type.lower() == 'staff':
                dojo.add_person(fname, lname, 'staff')
            elif person_type.lower() == 'fellow':
                if wants_accommodation not in ('y', 'Y'):
                    dojo.add_person(fname, lname, 'fellow')
                else:
                    dojo.add_person(fname, lname, 'fellow', 'y')
            else:
                cprint('Invalid!!! Dojo Occupants'
                       'are either Fellows or Staff', 'red')
        else:
            cprint('Names can only be string character', 'red')

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>
        """
        room_name = arg.get('<room_name>')
        dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [(-o <filename>)]
        """
        filename = arg.get('<filename>')
        if not (filename):
            dojo.print_allocations()
        else:
            dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [(-o <filename>)]
        """
        filename = arg.get('<filename>')
        if not (filename):
            dojo.print_unallocated()
        else:
            dojo.print_unallocated(filename)

    @docopt_cmd
    def do_people_id(self, arg):
        """Usage: people_id
        """
        dojo.people_id()

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <room_name>
        """
        person_id = arg.get('<person_identifier>')
        room_name = arg.get('<room_name>')
        if person_id.isdigit():
            person_id = int(person_id)
            dojo.reallocate_person(person_id, room_name)
        else:
            print('Person Id can only be an Integer')

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <filename>
        """
        text_file = arg.get('<filename>')
        dojo.load_people(text_file)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [(--db <sqlite_database>)]
        """
        db_name = arg.get('<sqlite_database>', None)
        if db_name:
            dojo.save_state(db_name)
        else:
            dojo.save_state()

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>
        """
        db_name = arg.get('<sqlite_database>')
        dojo.load_state(db_name)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        cprint('Dojo says Good Bye!', 'green')
        exit()


opt = docopt(__doc__, sys.argv[1:], version=1.0)

if not opt['--interactive'] or opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
