# PythonDebuggerTools

This is a collection of useful debugging tools to make your python development process faster.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PythonDebuggerTools.

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps PythonDebuggerTools==[latest-version]
```

## Usage

```py
from PythonDebuggerTools.logger import logger

@logger(important_params=['x', 'y'])
def add(x, y):
    return x + y
```

## Key-word arguments
* **important_params**
  * a python list of paramters to print in the debugging console
