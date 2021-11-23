import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.PythonDebuggerTools.logger import Log, Debug

f1_log = Log()
f1_log.DEBUG = True

f2_log = Log()
f2_log.DEBUG = False

def f1(a):
    # code that executes
    f1_log.log("Debug statements for function f1 that are printed")
    #continue execution of code

def f2(x, y):
    # code that executes
    f2_log.log("Debug statements for function f2 that are not printed!")


f1(1)
f2(1, 2)