#!/usr/bin/env python

'''import modules.'''
import os
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '../'))

MODELS_DIR = os.path.join(ROOT_DIR, 'models')
MANAGER_DIR = os.path.join(ROOT_DIR, 'manager')

sys.path.append(ROOT_DIR)
sys.path.append(MODELS_DIR)
sys.path.append(MANAGER_DIR)

from dojo import Dojo
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.office import Office 
from models.living import LivingSpace
from manager.roommanager import RoomManager

