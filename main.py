import sys
import os
import re
import tkinter as tk

# args: None
# returns: the type of operating system the current computer is running on, None if error
def operating_system():

    if sys.platform == "linux" or platform == "linux2":
        return "linux"

    elif sys.platform == "darwin":
        return "osx"

    elif sys.platform == "win32":
        return "windows"

    return None

# args: None
# returns: the path to the desktop on the current computer, None if error
def desktop_path(system):

    if system == None or (system != "linux" and system != "osx" and system != "windows"):
        # print("Invalid system argument.")
        return None

    # desktop from home directory
    if system == "linux" or system == "osx":
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    else:
        # on windows
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # check is valid path
    if not os.path.exists(desktop):
        return None

    return desktop

# args: None
# returns: the path to the created directory on the desktop
def create_folder(desk, name):

    if desk == None or (not os.path.exists(desk)) or name == None or name == "":
        # print("Invalid create folder arguments.")
        return None

    path = os.path.join(desk, name)

    if not os.path.exists(path):
        os.mkdir(path)

    return path

if __name__=="__main__":

    system = operating_system()

    if not system:
        sys.exit("Unable to identify operating system.")

    desk = desktop_path(system)

    if not desk:
        sys.exit("No desktop path found.")

    folder = create_folder(desk, "Cleaned")

    print("Main finished")
