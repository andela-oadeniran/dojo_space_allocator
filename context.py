#!/usr/bin/env python

#import modules
import os
import sys
DB_DIR = os.path.abspath(os.path.join(os.path.dirname(
    __file__), './db'))
MODELS_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), './models'))
MANAGER_DIR = os.path.abspath(os.path.join(os.path.dirname(
    __file__), './manager'))
sys.path.append(DB_DIR)
sys.path.append(MODELS_DIR)
sys.path.append(MANAGER_DIR)

from roommanager import RoomManager
from personmanager import PersonManager
# from models.fellow import Fellow
# from models.office import Office
# from models.room import Room
# from models.living import LivingSpace

