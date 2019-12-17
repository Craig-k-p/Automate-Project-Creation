#!/bin/bash


function new_project() {
    # Execute the following terminal commands when the command "new_project is typed into the terminal"

    # Make sure execution starts with the home directory as the cwd
    cd
    # execute create_project.py and provide access to the user-provided argument ($1)
    python3 ~/Documents/Projects/'Automate Project Creation'/create_project.py $1
}