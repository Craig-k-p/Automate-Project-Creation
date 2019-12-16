''' This file can be used to quickly setup the files needed to execute create_project.py
Steps:
    - create file .custom_commands.sh if it doesn't exist already
    - create file .create_project_settings.txt if it doesn't exist already
    - insert necessary lines in the .bashrc file
    - prompt the user for GitHub username, token, and the directory to place newly pulled repositories

'''

import os
import sys


def setup():

    create_files = ['.create_project_settings.txt', '.custom_commands.sh']
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

        # Create .custom_commands.txt
        if '.custom_commands.txt' in home_dir_objects:
            print('.custom_commands.txt already exists in the home directory.  Passing..')

        else:
            custom_commands_text = '''#!/bin/bash


function new_project() {
    # Execute the following terminal commands when the command "new_project is typed into the terminal"

    # Make sure execution starts with the home directory as the cwd
    cd
    # execute create_project.py and provide access to the user-provided argument ($1)
    python3 ~/Documents/Projects/'Automate Project Creation'/create_project.py $1
}'''

            with open(create_files[1], 'w') as file:
                file.write(custom_commands_text)

        # Create .create_project_settings.txt

        # Insert lines into .bashrc


if __name__ == '__main__':
    setup()
