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

#import necessary modules
import sys
import cmd
from docopt import docopt, DocoptExit




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
