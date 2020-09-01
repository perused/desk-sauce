from main import *

def test_operating_system():
    assert operating_system() == "linux"
    print("Passed operating system test")

test_operating_system()