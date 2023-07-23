import configparser
import datetime
from asyncio import sleep


def configMeManager():
    fileName = input('FileName?: \n$_')
    try:
        from configparser import ConfigParser
    except ImportError:
        from configparser import ConfigParser  # ver. < 3.0
    try:
        # instantiate
        config = ConfigParser()
        # parse existing file
        config.read('test.ini')
        # read values from a section
        string_val = config.get('section_a', 'string_val')
        print(config.get('section_a', 'string_val'))
        bool_val = config.getboolean('section_a', 'bool_val')
        int_val = config.getint('section_a', 'int_val')
        float_val = config.getfloat('section_a', 'pi_val')
        # update existing value
        config.set('section_a', 'string_val', 'world')
        # add a new section and some values
        config.add_section('section_b')
        config.set('section_b', 'meal_val', 'spam')
        config.set('section_b', 'not_found_val', '404')
    except configparser.DuplicateSectionError:
        print('err')
    with open('test.ini', 'w') as configfile:
        config.write(configfile)
    """configMeFile = new configparser.ConfigParser()
        configparser.add_section('user')
        configparser.add_section('organization')
        configparser.add_section('user')
def configMeManager(txt):
    while open(f"/log/configMe{datetime.datetime()}.ini",'w') as file:
        for line in file:
            if not line:
                line."""
configMeManager()