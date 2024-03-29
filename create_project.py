import getpass
import os
import sys
# PyGithub Module - Documentation: pygithub.readthedocs.io
import github


def newProject():

    # Grab the string passed from the terminal as the project name
    project_name = str(sys.argv[1])

    # Settings file for project folder path, GitHub username, token
    settings_file = '.create_project_settings.txt'

    # Get the user's personal access token, project path, and GitHub username from the settings file
    # try:
    with open(settings_file, 'r') as f:
        settings = f.readlines()
        # token = settings[3].strip()
        # Get the user's path for saving the new repository
        project_path = settings[5].strip()
        # Get the user's GitHub username
        github_username = settings[6].strip()
        # Change to the project directory
        os.chdir(project_path)

    g = github.Github(github_username, getpass.getpass(prompt=f'Password for GitHub user {github_username} >> '))

    # # If the file wasn't found, handle it nicely and provide a suggested remedy
    # except FileNotFoundError:
    #     print(f'"{settings_file}" was not found in the user\'s home directory')
    #     print(f'Please check the Readme file for instructions.  Ending execution..\n')
    #     return

    # If user input "token" is not blank use their input as the token
    # else:
    #     g = github.Github(token)

    # Check that the user credentials are valid by attempting to read the first repository
    try:
        g.get_user().get_repos()[0].name

    # If GitHub does not accept the user token end program execution
    except github.BadCredentialsException:
        print('Github token is invalid.  Ending execution..')
        return

    # Check if the directory already exists on the local computer
    if project_name in os.listdir():
        # The directory already exists, so report the error and stop the script
        print(f'Project directory {project_name} already exists on local computer.')
        return

    # Check if the repository already exists on the user's GitHub
    elif project_name in [repo.name for repo in g.get_user().get_repos()]:
        print(f'Project {project_name} already exists on GitHub.  Ending execution..\n')
        return

    else:
        # Print the existing repositories
        print(f'\n{project_name} not found. User repos found:')
        for repo in g.get_user().get_repos():
            print('\t-' + repo.name)

        # Make sure the user wants to create the repository
        if input(f'\nCreate new repository? [y] >> ') in ['', 'y', 'yes']:
            # Create a repo for the given user
            repo = g.get_user().create_repo(project_name)

            m1 = f'----{project_name.upper()} Readme----\n'
            m2 = 'Project generated by craig-k-p/Automate-Project-Creation'

            # Create a new file on the newly created repo
            # repo.create_file(file_name, commit_msg, file_content)
            repo.create_file('Readme.txt', 'Initial readme creation', m1 + m2)

            # Clone the repository to the current working directory
            os.system(f'git clone https://github.com/{github_username}/{project_name}')

        else:
            print('Repository creation cancelled\n')


newProject()
