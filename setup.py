''' This file can be used to quickly setup the files needed to execute create_project.py
Steps:
    - Move file temp.create_project_command.sh to home dir if it doesn't exist already
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


def setupSettings(user):

    while user['github_username'] is '':
        # Move temp.create_project_settings.txt to the home folder
        user['github_username'] = input('What is your GitHub username?  >> ')

    # Open a file selection dialog box and have the user select which directory new projects will be stored
    input('Please select the directory in which new projects will be stored. [open directory dialog]  >> ')
    try:
        user['new_project_dir'] = subprocess.check_output(
            ['zenity', '--file-selection', '--directory']
        ).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print('subprocess.CalledProcessError')

    return user


def getSetupFileData(user):

    # Open temp.create_project_settings.txt and write the user's preferred dir for
    # new projects and their GitHub username to the file
    with open(user['setup_dir'] + 'temp.create_project_settings.txt', 'r') as temp_settings:
        lines = temp_settings.readlines()
        lines.append(user['new_project_dir'] + '\n')
        lines.append(user['github_username'] + '\n')
        for l in lines:
            print(l)
        user['.create_project_settings.txt'] = lines

    # Open temp.bashrc and write the path to the parent dir of this script
    # for documentation
    with open(user['setup_dir'] + 'temp.bashrc', 'r') as temp_bashrc:
        lines = temp_bashrc.readlines()
        lines[1] = lines[1].replace('[path to file]', user['path_to_script'])
        user['temp.bashrc'] = lines

    # Open temp.create_project_command.txt and write the path to the parent
    # directory of this script so the command can find create_project.py
    with open(user['setup_dir'] + 'temp.create_project_command.txt', 'r') as temp_create_project_command:
        lines = temp_create_project_command.readlines()
        lines[9] = lines[9].replace('[path to script]', user['path_to_script'])
        user['.create_project_command.sh'] = lines

    return user


def backupBash(user):
    # Make a backup copy of .bashrc in the home directory
    bashrc_backed_up = False
    if '.bashrc' in user['home_dir_objects']:
        shutil.copyfile(user['home_dir'] + '.bashrc', user['home_dir'] + '.create_project.bashrc.backup')
        bashrc_backed_up = True
    else:
        print('.bashrc was not found in the home directory. A Bash shell is required for this program to work.')


def setupBash(user):
    # Open .bashrc and insert lines from temp.bashrc
    with open(user['home_dir'] + user['bashrc_file'], 'r') as bashrc:
        user['.bashrc'] = bashrc.readlines()

    if 'source ~/.create_project_command.sh' in user['.bashrc']:
        print('Skipping .bashrc')

    else:

        # Insert a blank line into the new lines
        user['temp.bashrc'].insert(0, '\n')
        user['temp.bashrc'].insert(len(user['temp.bashrc']), '\n')

        # This is a code snippet found near the top of the original .bashrc file
        # Use these to find some empty lines underneath to be sure the commands
        # don't get inserted into an "if" block
        test1 = 'case $- in\n'
        test2a = '    *i*) ;;\n'
        test2b = '\t*i*) ;;\n'  # test2b and test3b check for tabs instead of spaces
        test3a = '      *) return;;\n'
        test3b = '\t  *) return;;\n'
        test4 = 'esac\n'

        try:
            i1 = user['.bashrc'].index(test1)
            try:
                i2 = user['.bashrc'].index(test2a)
            except ValueError:
                i2 = user['.bashrc'].index(test2b)
            try:
                i3 = user['.bashrc'].index(test3a)
            except ValueError:
                i3 = user['.bashrc'].index(test3b)
            i4 = user['.bashrc'].index(test4)
        except('ValueError'):
            pass

        # Check if the lines found are in sequence
        if i1 < i2 < i3 < i4:
            # Insert new lines with surrounding blank lines
            i = i4
            for new_line in user['temp.bashrc']:
                i += 1
                user['.bashrc'].insert(i, new_line)


def writeFiles(user):
    with open(user['home_dir'] + '.create_project_settings.txt', 'w') as f:
        f.writelines(user['.create_project_settings.txt'])
    with open(user['home_dir'] + '.create_project_command.sh', 'w') as f:
        f.writelines(user['.create_project_command.sh'])
    with open(user['home_dir'] + '.bashrc', 'w') as bashrc:
        bashrc.writelines(user['.bashrc'])


def setup():
    user = {
        'home_dir': os.path.expanduser('~') + '/',
        'path_to_script': os.path.dirname(os.path.abspath(__file__)),
        'setup_files': [
            '.create_project.bashrc.backup',
            '.create_project_settings.txt',
            '.create_project_command.sh'],
        'bashrc_file': '.bashrc',  # Bash file that points to .create_project_command.sh
        'github_username': ''
    }
    user['home_dir_objects'] = os.listdir(user['home_dir'])
    user['setup_dir'] = user['path_to_script'] + '/setup/'

    print('This script will do the following:')
    print(f'''  -Insert a few lines in the file named "{user['bashrc_file']}" in your home directory''')
    print('  -Create/overwrite these hidden files in the home directory:')
    for file in user['setup_files']:
        print(f'    "{file}"')

    prompt = 'I accept that the above files will be overwritten if they exist. (yes) >> '
    if input(prompt).lower() in ('', 'y', 'yes'):

        print('Creating hidden files..')

        user = setupSettings(user)
        user = getSetupFileData(user)
        backupBash(user)
        setupBash(user)
        writeFiles(user)
        print('Setup complete')
        print()


if __name__ == '__main__':
    setup()
