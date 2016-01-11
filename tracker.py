# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:37:07 2016

@author: jamie
"""

import jsonobject
import jsonpickle
import logging
import string
import random
import uuid


TITLE = 'Item Tracker'
VERSION = '0.0.2'
AUTHOR = 'Jamie Paton'


class Location(jsonobject.JSONObject):
    def __init__(self, description, code=None):
        self.description = description
        self.code = code


class Item(jsonobject.JSONObject):
    def __init__(self, name, stored=False, location=None):
        self.name = name
        self.stored = stored
        self.location = location
        self.id = uuid.uuid4()


def generate_code(locations=None):
    characters = string.ascii_uppercase
    characters = characters.replace("I", "")
    characters = characters.replace("O", "")
    locations = Location.load_from_file("locations.json")
    if locations:
        while True:
            code = "{}{}".format(random.choice(characters),
                                 random.choice(characters))
            if code not in [location.code for location in locations]:
                break
    else:
        code = "{}{}".format(random.choice(characters),
                             random.choice(characters))
    return code


def add_item(item):
    items.append(item)
    with open('items.json', 'w') as f:
        f.write(jsonpickle.encode(items))


def add_location(location):
    locations = Location.load_from_file("locations.json")
    if location.code:
        locations.append(location)
    else:
        location.code = generate_code(locations)
        locations.append(location)
    with open('locations.json', 'w') as f:
        f.write(jsonpickle.encode(locations))


def save():
    with open('items.json', 'w') as f:
        f.write(jsonpickle.encode(items))
    with open('locations.json', 'w') as f:
        f.write(jsonpickle.encode(locations))

if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])
    items = []
    locations = Location.load_from_file("locations.json")
    print locations
#    add_item(Item("fish"))

    print generate_code()
