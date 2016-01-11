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


TITLE = 'tracker'
VERSION = '0.0.2'
AUTHOR = 'Jamie Paton'


characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = characters.replace("I", "")
characters = characters.replace("O", "")
print characters

print "{}{}".format(random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase))



class Item(jsonobject.JSONObject):
    def __init__(self, name, stored=False, location=None):
        self.name = name
        self.stored = stored
        self.location = location
        self.id = uuid.uuid4()

def add_item(item):
    items.append(item)
    save()

def save():
    with open('items.json', 'w') as f:
        f.write(jsonpickle.encode(items))

if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])
    items = []
    add_item(Item("fish"))
