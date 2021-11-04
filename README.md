# PythonDebuggerTools

This is a collection of useful debugging tools to make your python development process faster.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PythonDebuggerTools-0.0.16

```bash
pip install PythonDebuggerTools
```

## Usage
### Using the Debug.logger decorator

```py
from PythonDebuggerTools.logger import Debug

D = Debug()
D.DEBUG = True

@D.logger(important_params=['x', 'y'])
def add(x, y):
    return x + y
```

## Logger Key-word arguments
* **important_params**
  * a python list of paramaters to print in the standard output


### Using the Log module
```py
from PythonDebuggerTools.logger import Log

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

```

## Contribution Guidelines
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Github Repository
[PythonDebuggerTools Github Repository](https://github.com/Luna-Cake/Logger)