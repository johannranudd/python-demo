from typing import Final 

def constants_demo():
    print("==========constants==========")
    VERSION: Final[str] = "1.0.12"
    # VERSION = "2.0.0" // will work, only get error in the editor
    print(VERSION)