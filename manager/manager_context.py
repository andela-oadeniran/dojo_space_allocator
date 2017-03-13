#!/usr/bin/env python

'''import modules.'''
import os
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '../'))

MODELS_DIR = os.path.join(ROOT_DIR, 'models')


sys.path.append(ROOT_DIR)
sys.path.append(MODELS_DIR)

from models.fellow import Fellow
from models.office import Office
from models.living import LivingSpace
from models.person import Person
from models.room import Room
from models.staff import Staff
