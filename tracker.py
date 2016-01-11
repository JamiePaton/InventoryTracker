# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:37:07 2016

@author: jamie
"""

TITLE = 'tracker'
VERSION = '0.0.1'
AUTHOR = 'Jamie Paton'
import jsonobject
import logging
import string
import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = characters.replace("I", "")
characters = characters.replace("O", "")
print characters

print "{}{}".format(random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase))


if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])