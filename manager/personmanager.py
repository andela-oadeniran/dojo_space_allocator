#!/usr/bin/env/python

from manager_context import Fellow
from manager_context import Staff


class PersonManager():
    '''
    This manages all the details of persons in Dojo
    '''

    def __init__(self):
        pass

    def check_name_validity(fname, lname):
        if fname.isalpha().strip() and lname.isalpha().isalpha():
            return True
        else:
            raise  ValueError

    def check_valid_person_role(self, role):
        # check for valid input
        if role.lower() in ('staff', 'fellow'):
            return role
        else:
            raise TypeError

    def return_staff_fellow_class(self, role):
        # return the Fellow or Staff class used to create Fellow
        # and Staff instances
        return Staff if role.lower() == 'staff' else Fellow

    def add_person_to_session(self, person, people_list):
        # This function adds a valid user to the list of persons in Dojo
        people_list.append(person)
        self.person_id(person, people_list)
        return people_list

    def person_id(self, person, people_list):
        # This gets the id from the people length and
        # equate to the person's id
        person.id = len(people_list)
        return person.id


