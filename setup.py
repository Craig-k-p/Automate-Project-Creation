''' This file can be used to quickly setup the files needed to execute create_project.py
Steps:
    - Move file temp.custom_commands.sh to home dir if it doesn't exist already
        - Get path to create_project.py
    - Move file temp.create_project_settings.txt to home dir if it doesn't exist already
        - Get path to the default directory for project pulling
        - Get the user's GitHub username
    - backup .bashrc file
        - Change cwd? ".bashrc not found" in ./././Auto Pr. Cr.
    - insert necessary lines in the .bashrc file
    - prompt the user for GitHub username, token, and the directory to place newly pulled repositories

'''

import os
import shutil
import subprocess
import sys


def setupCustomCommands(user):
    # Move .custom_commands.txt
    if '.custom_commands.txt' in user['home_dir_objects']:
        print('.custom_commands.txt already exists in the home directory.  Passing..')

    else:
        # Move temp.custom_commands.sh to the home folder
        # shutil.move()
        print('Pretending to move temp.custom_commands.sh')


def setupSettings(user):
    # Move .create_project_settings.txt
    if '.create_project_settings.txt' in user['home_dir_objects']:
        print('.create_project_settings.txt already exists in the home directory.  Passing..')

    else:
        # Move temp.create_project_settings.txt to the home folder
        user['github_username'] = input('What is your GitHub username?  >> ')

        # Open a file selection dialog box and have the user select which directory new projects will be stored
        input('Please select the directory in which new projects will be stored. [continue]  >> ')
        try:
            user['new_project_dir'] = subprocess.check_output(
                ['zenity', '--file-selection', '--directory']
            ).decode('utf-8').strip()
            print(file)
        except subprocess.CalledProcessError:
            pass

        print(user['new_project_dir'])
        # shutil.move()
        print('Pretending to move temp.create_project_settings.txt')

    return user


def backupBash(user):
    # Make a backup copy of .bashrc in the home directory
    bashrc_backed_up = False
    if '.bashrc' in user['home_dir_objects']:

        if '.backup_create_project.bashrc' not in user['home_dir_objects']:
            shutil.copyfile(user['home_dir'] + '.bashrc', '.backup_create_project.bashrc')
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


def setupBash(user):
    # Open .bashrc and insert lines from temp.bashrc
    with open(user['home_dir'] + user['bashrc_file'], 'r') as bashrc:
        lines = bashrc.readlines()

    # Open temp.bashrc and read the lines
    with open(user['setup_dir'] + 'temp.bashrc', 'r') as temp_bashrc:
        new_lines = temp_bashrc.readlines()

    new_lines.insert(0, '\n')

    test1 = 'case $- in\n'
    test2a = '    *i*) ;;\n'
    test2b = '\t*i*) ;;\n'
    test3a = '      *) return;;\n'
    test3b = '\t  *) return;;\n'
    test4 = 'esac\n'

    try:
        i1 = lines.index(test1)
        try:
            i2 = lines.index(test2a)
        except ValueError:
            i2 = lines.index(test2b)
        try:
            i3 = lines.index(test3a)
        except ValueError:
            i3 = lines.index(test3b)
        i4 = lines.index(test4)
    except('ValueError'):
        pass

    if i1 < i2 < i3 < i4:
        i = i4
        for new_line in new_lines:
            i += 1
            lines.insert(i, new_line)

    n = 0
    for line in lines:
        print(str(n + 1) + '- ' + line)
        n += 1
        if n == 18:
            return


def modifySetupFiles(user):


def setup():

    fields2 = ' setup_dir home_dir_objects github_username new_project_dir'
    user = {
        'home_dir': os.path.expanduser('~') + '/',
        'path_to_script': os.path.dirname(os.path.abspath(__file__)),
        'setup_files': ['.backup_create_project.bashrc', '.create_project_settings.txt', '.custom_commands.sh'],
        'bashrc_file': 'test.bashrc'  # Bash file that points to .custom_commands.sh
    }
    user['home_dir_objects'] = os.listdir(user['home_dir'])
    user['setup_dir'] = user['path_to_script'] + '/setup/'
    print(user['home_dir_objects'])

    print('This script will do the following:')
    print(f'''  -Insert a few lines in the file named "{user['bashrc_file']}" in your home directory''')
    print('  -Create these hidden files in the home directory if they don\'t exist:')
    for file in user['setup_files']:
        print(f'    "{file}"')

    if input('Proceed? (yes)').lower() in ('', 'y', 'yes'):

        print('Creating hidden files..')

        print()
        setupCustomCommands(user)
        print()
        user = setupSettings(user)
        print()
        backupBash(user)
        print()
        setupBash(user)
        print('Setup complete')
        print()


if __name__ == '__main__':
    setup()
