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
from models.person import Person, Fellow, Staff
from models.room import Room, Office, LivingSpace
# from manager.roommanager import RoomManager

