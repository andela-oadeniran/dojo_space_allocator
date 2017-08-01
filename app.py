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

    def fn(self, args):
        try:
            opt = docopt(fn.__doc__, args)

        except DocoptExit as e:
            # This is thrown if a false command is given.
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # Exception calls app.py help.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    fig_font = Figlet(font='graffiti')
    welcome_text = fig_font.renderText('Dojo Space Allocator')
    welcome_text = colored(
        welcome_text, 'green') + colored(
        'Type help to get commands', 'magenta')
    intro = welcome_text
    prompt = colored('dojo>>>', 'cyan')
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_names>...
        """
        room_type = args.get('<room_type>')
        room_names = args.get('<room_names>')
        dojo.create_room(room_type, room_names)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <fname> <lname> <FELLOW/STAFF> [<wants_accommodation>]
        """
        fname = args.get('<fname>')
        lname = args.get('<lname>')
        person_role = args.get('<FELLOW/STAFF>')
        wants_accommodation = args.get('<wants_accommodation>', None)
        dojo.add_person(fname, lname, person_role, wants_accommodation)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>
        """
        room_name = args.get('<room_name>')
        dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [(-o <filename>)]
        """
        filename = args.get('<filename>', None)
        dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [(-o <filename>)]
        """
        filename = args.get('<filename>', None)
        dojo.print_unallocated(filename)

    @docopt_cmd
    def do_people_id(self, args):
        """Usage: people_id
        """
        dojo.people_id()

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_identifier> <room_name>
        """
        person_id = args.get('<person_identifier>')
        room_name = args.get('<room_name>')
        if person_id.isdigit():
            person_id = int(person_id)
            dojo.reallocate_person(person_id, room_name)
        else:
            print('Person Id can only be an Integer')

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>
        """
        text_file = args.get('<filename>')
        dojo.load_people(text_file)

    @docopt_cmd
    def do_save_state(self, args):
        """Usage: save_state [(--db <sqlite_database>)]
        """
        db_name = args.get('<sqlite_database>')
        if not db_name:
            dojo.save_state()
        else:
            dojo.save_state(db_name)

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: load_state <sqlite_database>
        """
        db_name = args.get('<sqlite_database>')
        dojo.load_state(db_name)

    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        cprint('Dojo says Good Bye!', 'green')
        exit()


opt = docopt(__doc__, sys.argv[1:], version=1.0)

if not opt['--interactive'] or opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
