from main import *
import os

def test_operating_system():

    assert operating_system() == "linux", "Failed operating system test a"
    assert sys.platform == "linux" or platform == "linux2", "Failed operating system test b"
    
    print("Passed operating system tests.")

def test_desktop_path():

    assert desktop_path("linux") == "/home/sam/Desktop", "Failed desktop path test a"
    assert desktop_path(None) == None, "Failed desktop path test b"
    assert desktop_path("blah") == None, "Failed desktop path test c"

    print("Passed desktop path tests.")

def test_create_folder():
    # regular tests of creating folders
    assert create_folder(desktop_path("linux"), "Cleaned") == "/home/sam/Desktop/Cleaned", "Failed create folder test a"
    assert os.path.exists("/home/sam/Desktop/Cleaned"), "Failed create folder test b"
    os.rmdir("/home/sam/Desktop/Cleaned")

    assert create_folder(desktop_path("linux"), "Blah") == "/home/sam/Desktop/Blah", "Failed create folder test c"
    assert os.path.exists("/home/sam/Desktop/Blah"), "Failed create folder test d"
    os.rmdir("/home/sam/Desktop/Blah")

    assert create_folder(desktop_path("linux"), "with space") == "/home/sam/Desktop/with space", "Failed create folder test e"
    assert os.path.exists("/home/sam/Desktop/with space"), "Failed create folder test f"

    # testing that already created folder works
    assert create_folder(desktop_path("linux"), "with space") == "/home/sam/Desktop/with space", "Failed create folder test g"
    assert os.path.exists("/home/sam/Desktop/with space"), "Failed create folder test h"
    os.rmdir("/home/sam/Desktop/with space")

    # testing invalid arguments
    assert create_folder(desktop_path("linux"), "") == None, "Failed create folder test i"
    assert create_folder(desktop_path("linux"), None) == None, "Failed create folder test j"
    assert create_folder("Blah", "Blah") == None, "Failed create folder test k"
    assert create_folder(None, "Blah") == None, "Failed create folder test l"

    print("Passed create folder tests.")

test_operating_system()
test_desktop_path()
test_create_folder()
print("Finished tests.\n")