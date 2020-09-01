import sys
import os
import re
import tkinter as tk

SYSTEM = ""

def operating_system():

    if sys.platform == "linux" or platform == "linux2":
        SYSTEM = "linux"

    elif sys.platform == "darwin":
        SYSTEM = "osx"

    elif sys.platform == "win32":
        SYSTEM = "windows"

# args: None
# returns: the path to the desktop on the current computer
def desktop_path():

    # desktop from home directory on unix/linux
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # on windows
    # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


    # check is valid path


    # if not found or invalid, program fails
    return None

if __name__=="__main__":

    desk = desktop_path()

    if not desk:
        sys.exit("No desktop path found.")

    print("Success")
