# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:53:05 2016

@author: jamie
"""
import sys
import os
import tracker
import logging
from msvcrt import getch
import pprint

TITLE = 'Inventory Tracker'
VERSION = '0.0.1'
AUTHOR = 'Jamie Paton'

def setup_logging(default_path='logs/loggingconfig.json', default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration

    """
    import os
    import json
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def imports():
    import types
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__

def main(args):
    while True:
        os.system('cls')
        print "1.    add item    --- NOT IMPLEMENTED YET"
        print "2.    add location"
        print "3.    show locations"
        option = getch()
#        option = raw_input(">>>")
        if option == "1":
            pass
        elif option == "2":
            description = raw_input("enter location description:\t")
            number = int(raw_input("enter number of locations at this description:\t"))
            for _ in xrange(number):
                tracker.add_location(tracker.Location(description))
        elif option == "3":
            locations = tracker.Location.load_from_file('locations.json')
            codes = {}
            for location in locations:
                if location.description not in codes:
                    codes[location.description] = [location.code]
                else:
                    codes[location.description].append(location.code)
            pprint.pprint(codes)
            raw_input()
        elif option == "q":
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))