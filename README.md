[![Coverage Status](https://coveralls.io/repos/github/andela-oadeniran/dojo_space_allocator/badge.svg)](https://coveralls.io/github/andela-oadeniran/dojo_space_allocator)
[![Build Status](https://travis-ci.org/andela-oadeniran/dojo_space_allocator.svg?branch=master)](https://travis-ci.org/andela-oadeniran/dojo_space_allocator)


##            Dojo Space Allocator.

### The Application and what it does?
1. A Console Application that helps allocate an office space, room space or both.
2. The Dojo is one of Andela's facility in Kenya and it inspired the Application.

###  How to Use
1. Clone the repository or download the zip file.
2. install python3, virtualenvwrapper.
3. install application's requirements with pip install -r requirements.txt

###   Commands
 1. create_room room_type room_name `Use the command to create a room.`
 2. add_person fname lname STAFF/FELLOW [wants-accommodation]
  `Used to add a person to the System and if available an office and for a fellow who wants accommodation a Living Space.`
 3. print_room room_name `To print the occupants in a particular room`
 4. print_allocations `To print each room and the corresponding room members`
 5. print_unallocated `To print the number of people without an Allocated Office and or Living Space`
 6. people_id `To print the ID corresponding to each person`
 7. reallocate_person person_id room_name `This command helps to either reallocate a person to another office or living space or allocate an unallocated person to an appropriate room.`
 8. load_people `The command helps load a list of persons(add a list) from a text file`
 9. save_state [--db sqlitedatabase] `saves the session data into an sqlite database`
 10. load_state sqlite-database-name `loads data from the database name specified.`