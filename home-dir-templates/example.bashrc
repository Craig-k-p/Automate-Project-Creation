# ---- Slice of .bashrc meant to be an example
# ---- Be sure to only add lines 11 or 9 thru 11 to your file

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# ----- Add the following 3 lines to your .bashrc file:
# Add custom commands to the shell
# Currently used for [path to file]/create_project.py
source ~/.custom_commands.sh


# append to the history file, don't overwrite it
shopt -s histappend