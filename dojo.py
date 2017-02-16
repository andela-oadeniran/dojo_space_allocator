

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
<<<<<<< HEAD
        valid_rooms = ['office','living']
        if room_type.lower()== 'office':
            for index, room_name in enumerate(room_names):
                room_data = {}
                if (unique_name(room_name, 'room')):
                    key_name = room_name
                    room_name = create_room(room_name, 'office')
                    room_data['room_name'] = room_name.room_name
                    room_data['room_type'] = room_name.room_type
                    room_data['room_occupants'] = room_name.room_occupants
                    room_data['max_occupants'] = room_name.maxoccupant
                    room_data['room_size'] = room_name.add_room_size()
                    app_session['room'].append(room_data)
                    print('An Office called {0} has been successfully created!'.format(room_data['room_name']))
                else:
                    print('{0} already exists can you name it something else'.format(room_name))
        elif room_type.lower() == 'living':
            for index, room_name in enumerate(room_names):
                room_data = {}
                if (unique_name(room_name, 'room')):
                    key_name = room_name
                    room_name = create_room(room_name, 'living')
                    room_data['room_name'] = room_name.room_name
                    room_data['room_type'] = room_name.room_type
                    room_data['room_occupants'] = room_name.room_occupants
                    room_data['max_occupants'] = room_name.maxoccupant
                    room_data['room_size'] = room_name.add_room_size()
                    app_session['room'].append(room_data)
                    print('A LivingSpace called {0} has been successfully created!'.format(room_data['room_name']))
=======
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
>>>>>>> ladi
                else:
                    print('{0} already exists can you name it something else'.format(room_name))


        else:
            raise TypeError
        return rooms

    def add_person(self, fname, lname, person_type, wants_accommodation='n'):
        valid_persons = ['fellow', 'staff']
        if (person_type.lower() == 'fellow') and (wants_accommodation.lower() == 'y' or wants_accommodation.lower()== 'yes'):
            person_data = {}
            person_name = '{0} {1}'.format(fname, lname)
            if (unique_name(person_name, 'person')):
                key_name = person_name
                person_name = create_person(person_name, 'fellow', 'y')
                person_data['person_name'] = key_name
                person_data['person_type'] = 'fellow'
                room_name = add_person_to_room(key_name, 'n')
                person_data['person_office'] = room_name
                living_name = add_person_to_room(key_name, 'y')
                person_data['person_living'] = living_name
                app_session['person'].append(person_data)
                print('Fellow {0} has been successfully added'.format(key_name))
                if room_name.strip() != '':
                    print ('{0} has been allocated the office {1}'.format(fname, room_name))
                if room_name.strip() != '':
                    print ('{0} has been allocated a livingspace {1}'.format(fname, living_name))
            else:
                answer = input('person already exists, are you sure this is a new person? "y" or "n"')
                if answer.lower()  == 'y':
                    key_name = person_name
                    person_name = create_person(person_name, 'fellow', 'y')
                    person_data['person_name'] = key_name
                    person_data['person_type'] = 'fellow'

                    room_name = add_person_to_room(key_name, 'n')
                    person_data['person_office'] = room_name
                    living_name = add_person_to_room(key_name, 'y')
                    person_data['person_living'] = living_name
                    app_session['person'].append(person_data)
                    print('Fellow {0} has been successfully added'.format(key_name))
                    if room_name.strip() != '':
                        print ('{0} has been allocated the office {1}'.format(fname, room_name))
                    if room_name.strip() != '':
                        print ('{0} has been allocated a livingspace {}'.format(fname, living_name))
                else:
                    print('Person not added')




        elif person_type.lower()=='fellow':
            person_data = {}
            person_name = '{0} {1}'.format(fname, lname)
            if (unique_name(person_name, 'person')):
                key_name = person_name
                person_name = create_person(person_name, 'fellow', 'n')
                person_data['person_name'] =  person_name.person_name
                person_data['person_type'] = person_name.person_type
                room_name = add_person_to_room(key_name, 'n')
                living_name = ''
                person_data['person_office'] = room_name
                person_data['person_living'] = None
                app_session['person'].append(person_data)
                print('Fellow {0} has been successfully added'.format(key_name))
                if room_name.strip() != '':
                    print ('{0} has been allocated the office {1}'.format(fname, room_name))
            else:
                answer = input('person already exists, are you sure this is a new person? "y" or "n"')
                if answer.lower == 'y':
                    key_name = person_name
                    person_name = create_person(key_name, 'fellow', 'n')
                    person_data['person_name'] =  person_name.person_name
                    person_data['person_type'] = person_name.person_type
                    room_name = add_person_to_room(key_name, 'n')
                    living_name = ''
                    person_data['person_office'] = room_name
                    person_data['person_living'] = None
                    app_session['person'].append(person_data)
                    print('Fellow {0} has been successfully added'.format(key_name))
                    if room_name.strip() != '':
                        print ('{0} has been allocated the office {1}'.format(fname, room_name))




        elif person_type.lower() == 'staff':
            person_data = {}
            person_name = '{0} {1}'.format(fname, lname)
            if (unique_name(person_name, 'person')):
                key_name = person_name
                person_name = create_person(person_name, 'staff', 'n')
                person_data['person_name'] = person_name.person_name
                person_data['person_type'] = person_name.person_type
<<<<<<< HEAD
=======
                # person_data['person_room'] = person_name.person_room
                #get room you want to add the person too from db / datastructure the details are stored
                # print(person_name)
                Dojo.app_session['person'].append(person_data)
                print(Dojo.app_session['person'])
                print("added staff")
>>>>>>> ladi
                room_name = add_person_to_room(key_name, 'n')
                person_data['person_office'] = room_name
                person_data['person_living'] = None
                app_session['person'].append(person_data)

                app_session['person'].append(person_data)
                print('Staff {0} has been successfully added'.format(key_name))
                if room_name.strip() != '':
                    print ('{0} has been allocated the office {1}'.format(fname, room_name))
            else:
                answer = input('Name already exists, are you sure this is a different person? "y" or "n"')
                if(answer.lower() == 'y'):
                    key_name = person_name
                    person_name = create_person(key_name, 'fellow', 'n')
                    person_data['person_name'] =  person_name.person_name
                    person_data['person_type'] = person_name.person_type
                    room_name = add_person_to_room(key_name, 'n')
                    person_data['person_office'] = room_name
                    person_data['person_living'] = None
                    app_session['person'].append(person_data)
                    print('Fellow {0} has been successfully added'.format(key_name))
                    if room_name.strip() != '':
                        print ('{0} has been allocated the office {1}'.format(fname, room_name))
                else:
                    print ("Person not added")



        else:
            raise TypeError
    def print_room(self, room_name):
        if len(app_session['room']) != 0:
            for index, value in enumerate(app_session['room']):
                if (value['room_name'] == room_name):
                    print('......................printing room occupants')
                    print (value['room_occupants'])
                    break
            else:
                print(("{0} not found").format(room_name))
        else:
            print ('No room is currently created')

    def print_allocations(self, to_file='n'):
        if to_file == 'n':
            if len(app_session['room']) != 0:
                for index, value in enumerate(app_session['room']):
                    if len(value['room_occupants']) != 0:
                        occupants =  ', '.join(value['room_occupants'])
                        print('.........just a moment')
                        print('           '+value['room_name'].upper())
                        print('---------------------------------------------------------')
                        print(occupants)
                    else:
                        print("This room is presently empty")
            else:
                print ('We currently do not have any room created. You can create a room using\
                    create_room room_type room_names')
        else:
            #write the data to file
            for index, value in enumerate(app_session['room']):
                occupants = ',  '.join(value['room_occupants'])
                file = open(to_file, 'a')
                file.write(value['room_name'].upper()+ '\n')
                file.write('------------------------------------ \n')
                file.write(occupants+ '\n')
                file.close()





    def print_unallocated(self, to_file='n'):
        if to_file == 'n':
            for index, value in enumerate(app_session['person']):
                if value['person_office'].strip() == '':
                    print ('{0} does not have an office yet'.format(value['person_name']))
                    if value['person_living']:
                        print ('{0} has been on the waiting list for a Living Space'.format(value['person_name']))
        else:
            #write to file
            for index, value in enumerate(app_session['person']):
                if (value['person_living']).strip() == '':
                    if value['person_office'].strip() == '':
                        file = open(to_file, 'a')
                        file.write('{0} wants an Office'.format(value['person_name'])+ '\n')
                        file.write('{0} wants a Living Space also.'.format(value['person_name']))
                        file.close
                    else:
                        file




    def reallocate_person(self, person_name, room_name):
        pass

    def load_people(self):
        pass

    def save_state(self):
        pass

    def load_state(self, db_sql):
        pass





#functions used by the methods in the dojo class
#
#       FUNCTION NAME                   FUNCTION USE
#
#
#
#



<<<<<<< HEAD
#function to check if a room name or person name already exists
def unique_name(name, app_session_key):
    unique_arr = []
    if app_session_key == 'room':
        for index, value in enumerate(app_session['room']):
            unique_arr.append(value['room_name'])
        if (name in unique_arr):
            return False
        else:
            return True
    else:
        for index, value in enumerate(app_session['person']):
            unique_arr.append(value['person_name'])
        if (name in unique_arr):
            return False
        else:
            return True
=======
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
>>>>>>> ladi


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
        return person_name

    elif person_type == 'fellow' and wants_accommodation=='n':
        person_name = Fellow(person_name)
        print(' doesn\'t want an accommodation and specified properly ')
        return person_name
    elif person_type == 'fellow' and wants_accommodation!='n':
        person_name = Fellow(person_name)
        print(' not added to living Space valid argument is "y" or "yes"')
        return person_name
    elif person_type == 'staff' and wants_accommodation=='n':
        # get instance of the staff class and pass the appropriate arguments to db/data_structure
        person_name = Staff(person_name)
        print("staff added with the appropriate argument for wants_accommodation")
        return person_name

    else:
        person_name = Staff(person_name)
        print("Living rooms are only available for fellows ")

#function to check whether a room is full

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
<<<<<<< HEAD
        for index, value in enumerate(app_session['room']):
            if(value['room_type'] =='office' and (value['room_size'] < value['max_occupants'])):
=======
        for index, value in enumerate(Dojo.app_session['room']):
            print(value)
            if(value['room_size'] < value['max_occupants']):
>>>>>>> ladi
                value['room_occupants'].append(person_name)
                value['room_size'] += 1
                print(value['room_occupants'])
                print(value)
                return value['room_name']
                break
        else:
            print("well I think we need more offices")
            return ""
    else:
        for index, value in enumerate(app_session['room']):
            if (value['room_type']=='living' and (value['room_size'] <  value['max_occupants'])):
                value['room_occupants'].append(person_name)
                value['room_size'] += 1
                print(value['room_occupants'])
                print(value)
                return value['room_name']
                break
        else:
            print("You have been placed on the waiting list")
            return ""




# Dojo().create_room('office', ['blue'])
# Dojo().create_room('living', ['blue', 'black', 'brown'])
# Dojo().add_person('ladi', 'adeniran', 'fellow')
# Dojo().add_person("oladipupo", "adeniran", "fellow")
# Dojo().add_person("oladipupo", "adeniran", "staff")

# Dojo().add_person("adeniran", "ladipupo", "fellow", "y")
# Dojo().add_person('ladi', 'adeniran', 'fellow', 'y')
# Dojo().print_room('blue')
# Dojo().print_allocations()
# Dojo().print_unallocated()




<<<<<<< HEAD

=======
>>>>>>> ladi













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

<<<<<<< HEAD

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
    # def do_print_room(self, arg):
    #     """Usa
    #     """
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
=======
>>>>>>> ladi
