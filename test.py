from main import *
import os

def test_operating_system():
    assert operating_system() == "linux", "Failed operating system test a"
    assert sys.platform == "linux" or platform == "linux2", "Failed operating system test b"
    print("Passed operating system test")

def test_desktop_path():
    assert desktop_path("linux") == "/home/sam/Desktop", "Failed desktop path test a"
    print("Passed desktop path test")

test_operating_system()
test_desktop_path()
print()