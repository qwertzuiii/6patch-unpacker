import sys
import os

from data.libraries import crypt_system as cryptsys
from data.libraries import command_system as csys
from data.libraries import extract_zip as extzip
# from data.libraries import json_load as jsonlib

arg = sys.argv
# cfg = jsonlib.get_json_data('data/config/application.json')
from data.config import application as cfg
key = 0x5A7C3

fileend = '.6patch'


prln = csys.console(f"[{cfg.prefixname}]").print

def head(add_begin_space = True, add_end_space = False, lines="=", lines_val=60):
    if add_begin_space:
        print()
    h = f"""{cfg.name} (v{cfg.version}) - developed by {cfg.creator}"""

    if lines != None:
        print(lines * lines_val)
    print(h)
    if lines != None:
        print(lines * lines_val)
    
    if add_end_space:
        print()

def start():
    head(True, True)

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
            return
    
    if csys._check_argument_exists(arg, '/nounpack'):  # Check if argument /nounpack is in arugments
        no_unpack = True
    else:
        no_unpack = False
    
    # Start de-/encrypting
    if not create:
        prln('Decrypting...')
    else:
        prln('Encrypting...')

    tempname = ".TEMP"
    tempfile = file + tempname
    cryptsys.crypt_file(file, tempfile, key)
    
    if create:
        prln('Renaming file...')

        if ".zip" in file:
            replc = file.replace('.zip', fileend)
        else:
            replc = file + fileend
        os.rename(tempfile, replc)
        return

    if not create:
        prln('Setting up file information...')
        
        if not "\\" in file:
            directory = file.replace(fileend, '')
            file_name = file
        else:
            file_split = file.split("\\")
            file_len = len(file_split) - 1
            file_p = ""

            for i in range(file_len):
                file_p += file_split[i] + "\\"

            file_name = file_split[file_len]
            directory = file_p + file_name.replace(fileend, '')

        if not no_unpack:
            prln('Creating extraction folder...')
            extzip.make_extraction_folder(directory)
            prln('Extracting...')
            extzip.extract_zip(tempfile, directory)
            prln('Removing temporary files...')
            os.remove(tempfile)
        else:
            prln('Renaming file...')
            os.rename(tempfile, file + '.zip')
        return



if __name__ == '__main__':
    start()

    prln('Finished')