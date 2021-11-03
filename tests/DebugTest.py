import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.PythonDebuggerTools.logger import Debug

Debugger = Debug()



Debugger.log("This statement must be printed")
Debugger.DEBUG = False
Debugger.log("This statement should not be printed")
Debugger.DEBUG = True
Debugger.log("This statement should be printed")
