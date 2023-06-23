import sys
import os

from data.libraries import crypt_system as cryptsys
from data.libraries import command_system as csys
from data.libraries import json_load as jsonlib

arg = sys.argv
cfg = jsonlib.get_json_data('data/config/application.json')
key = 0x5A7C3

fileend = '.6patch'

def head(add_begin_space = True, add_end_space = False, lines="=", lines_val=60):
    if add_begin_space:
        print()
    h = f"""{cfg['name']} (v{cfg['version']}) - developed by {cfg['creator']}"""

    if lines != None:
        print(lines * lines_val)
    print(h)
    if lines != None:
        print(lines * lines_val)
    
    if add_end_space:
        print()

def start():
    head(True)

    if len(arg) < 3:  # If not enough arguments
        print('Error: Invalid arguments')
        return
    
    if csys._check_argument_exists(arg, '-f'):  # Set File (index)
        file = csys._get_argument_index(arg, '-f')
    else:
        print('Error: Invalid arguments')
        return

    if file == None:  # Check if file is set in arguments
        print('Error: No file specified')
        return
    else:
        file = arg[file]  # Set file (text)


    if csys._check_argument_exists(arg, '/create'):  # Check if argument /create is in arugments
        create = True
    else:
        create = False

        if not file.endswith(fileend):  # Check if no /create and file is no {fileend} file
            print(f'Error: Is not a {fileend} file')
    
    # Start de-/encrypting
    tempname = ".TEMP"
    cryptsys.crypt_file(file, file + tempname, key)
    
    if create:
        os.rename(file + tempname, file + fileend)


if __name__ == '__main__':
    start()