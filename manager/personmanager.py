#!/usr/bin/env/python

from manager_context import Fellow
from manager_context import Staff


class PersonManager():
    '''
    This manages all the details of persons in Dojo
    '''

    def __init__(self):
        pass

    def check_name_validity(self, fname, lname):
        if fname.isalpha() and lname.isalpha():
            return True
        else:
            raise ValueError

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
        self.assign_id(person, people_list)
        return people_list

    def assign_id(self, person, people_list):
        # This gets the id from the people length and
        # equate to the person's id
        person.id = len(people_list)
        return person.id

    def assign_person_room_name(self, room, person):
        # this function assign to the per son object
        # the approprate room name attribut
        if room.room_type == 'office':
            person.office = room.name
        else:
            person.living_space = room.name

    def unallocated_list(self, people_list):
        office_unallocated = [person for person in people_list
                              if not person.office]
        fellow_list = [person for person in people_list
                       if person.role.lower() == 'fellow']
        living_space_unallocated = [person for person in fellow_list
                                    if person.wants_accommodation.lower() ==
                                    'y' and not(person.living_space)]
        return [office_unallocated, living_space_unallocated]

    def string_people_list(self, people_list):
        # It returns a list of person information i.e fname, lname and role.
        people_str_list = [person.pname for person in people_list]
        return people_str_list





