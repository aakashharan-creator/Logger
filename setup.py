from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Debugging tools'
LONG_DESCRIPTION = 'A package that gives users access to several debugging functionality to make their development process efficient.'

# Setting up
setup(
    name='logger',
    version=VERSION,
    author='Aakash Haran',
    author_email='aakash.haran01@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Luna-Cake/Logger',
    license='MIT',
    packages=['logger'],
    install_requires=[],
)