# PythonDebuggerTools

This is a collection of useful debugging tools to make your python development process faster.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PythonDebuggerTools-0.0.15

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps PythonDebuggerTools==[latest-version]
```

## Usage

```py
from PythonDebuggerTools.logger import Debug

D = Debug()
D.DEBUG = True

@D.logger(important_params=['x', 'y'])
def add(x, y):
    D.log("Here's a print statement than can
    be turned off by toggling D.DEBUG!")
    
    return x + y
```

## Logger Key-word arguments
* **important_params**
  * a python list of paramaters to print in the standard output

## Contributing Guidelines
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Github Repository
[PythonDebuggerTools Github Repository](https://github.com/Luna-Cake/Logger)