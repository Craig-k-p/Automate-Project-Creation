''' This file can be used to quickly setup the files needed to execute create_project.py
Steps:
    - create file .custom_commands.sh if it doesn't exist already
    - create file .create_project_settings.txt if it doesn't exist already
    - DONE backup .bashrc file
    - insert necessary lines in the .bashrc file
    - prompt the user for GitHub username, token, and the directory to place newly pulled repositories

'''

import os
import sys
import shutil


def setup():

    bashrc_file = 'test.bashrc'

    print('This script will do the following:')
    print('  -Create these hidden files in the home directory if they don\'t exist:')

    for file in create_files:
        print(f'    "{file}"')

    print(f'  -Create a backup copy of "{bashrc_file}" named ".backup{bashrc_file}" in the home directory')
    print(f'  -Insert a few lines in the file named "{bashrc_file}" in your home directory')

    if input('Proceed? (yes)') in ('', 'y', 'yes'):

        print('Creating hidden files..')

        home_dir = os.path.expanduser('~')
        home_dir_objects = os.lisdir(home_dir)
        print(obj)
        print(os.getcwd())

        # Create .custom_commands.txt
        if '.custom_commands.txt' in home_dir_objects:
            print('.custom_commands.txt already exists in the home directory.  Passing..')

        else:
            # Move temp.custom_commands.sh to the home folder
            # shutil.move()
            pass

        # Create .create_project_settings.txt
        if '.create_project_settings.txt' in home_dir_objects:
            print('.create_project_settings.txt already exists in the home directory.  Passing..')

        else:
            # Move temp.create_project_settings.txt to the home folder
            # shutil.move()
            pass

        # Make a backup copy of .bashrc in the home directory
        bashrc_backed_up = False
        if '.bashrc' in home_dir_objects:

            if '.backup_create_project.bashrc' not in home_dir_objects:
                shutil.copyfile('.bashrc', '.backup_create_project.bashrc')
                bashrc_backed_up = True

            else:
                print('".backup_create_project.bashrc" already exists.  Overwrite?')
                user_input = ''

                while user_input not in ('n', 'no', 'y', 'yes'):
                    user_input = input(' >>> ')

                if user_input.lower() in ('n', 'no'):
                    print('passing..')

                elif user_input.lower() in ('y', 'yes'):
                    print('Overwriting ".backup_create_project.bashrc"..')
                    shutil.copyfile('.bashrc', '.backup_create_project.bashrc')
                    bashrc_backed_up = True

                else:
                    print('Did not receive input "y", "n", "yes", or "no".  Passing..')

        else:
            print('.bashrc was not found in the home directory. A Bash shell is required for this program to work.')

        # Insert lines into .bashrc
        with open(bashrc_file, 'rw') as file:
            lines = file.readlines()


if __name__ == '__main__':
    setup()
