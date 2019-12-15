# Automate-Project-Creation 

This project is designed to allow the user to use the "create_project [project_name]"
command in a Bash terminal to create a new repository on GitHub and pull it to the
local computer to save time.  The command works for any user that follows the readme file
instructions.

Requirements:
	-Bash terminal
	-Git can communicate with GitHub on your Bash terminal
	-Ubuntu or other Linux distro


Setup instructions:

- Download this repository and note the file path from your home directory

- Find the "template.custom_commands.sh" file in the "home-dir-templates" directory
and replace the prompt with the path to "create_project.py"

- Move the above file to your home directory and rename it to ".custom_commands.sh"

- Find the file named "example.bashrc" in "home-dir-templates" and follow the
instructions in the file to add lines to ".bashrc" found in your home directory.  Use
ctrl + h (Ubuntu 19.10) to show hidden files.

- Find the file named "template.create_project_settings.txt" in "home-dir-templates"
and replace the last three lines with the appropriate information

- Move the above file to your home directory and rename it 
".create_project_settings.txt"

-Use new_project [project name] to create a new GitHub repo and pull it to your
computer!