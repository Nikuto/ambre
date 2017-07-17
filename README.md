# ambre

## Setting the working environment
We need few tools in order to setup a proper environment, be able to build (produce the wheel file) and install the project (from a .whl file, put our sources and the dependencies in one of the PYTHONPATH variable's directory).

What's a python wheel ?
> A built-package format for Python.  
A wheel is a ZIP-format archive with a specially formatted filename and the .whl extension.  

We'll use a virtualenv to keep a clean working environment and not be annoyed by dependency issues.
>virtualenv is a tool to create isolated Python environments.  
>The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application >that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you >install everything into /usr/lib/python2.7/site-packages (or whatever your platform’s standard location is), it’s easy to end up >in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.

A virtualenv in itself is a directory with another directory called scripts to activate this env, there is another directory lib where will be installed the different python package (the dependencies for example)  

To create a virtualenv:
```bash
virtualenv path/to/the/virtualenv
```
To activate it and gain access to the benefits of using a one:  
*On Unix systems*
```bash
source path/to/venv/bin/activate # or the right activation file according to your shell
```
*On windows*
```powershell
\path\to\venv\Scripts\activate
```  

Once activated every packages installed will be located in the virtualenv's site-packages directory (/venv/lib/python3.4/site-packages for a virtualenv named venv with python3.4).  
The tool used to install external packages is pip and is shipped with python. When building the project, all the python packages needed are automatically downloaded, the external dependencies such as a C library aren't though.  
Some packages will be used to statically check the code or give the coverage of the tests thus, type the following command to get all the required tools:
```bash
pip install -r requirements.txt
```  
You should now have all the tools we'll used for the project  

## Building and installation of the project  
Our project is no different than any other dependencies we could use, it's a python package thus will be builded using wheel and installed via pip  
To build the project use:
```bash
python setup.py bdist_wheel # create a wheel in a newly created dist directory
```
To install it use:
```bash
pip install -U dist/ambre-0.0-py3-none-any.whl # the filename change every version
```  
You should now see the installed package in your virtualenv under /venv/lib/python3.4/site-packages/ambre/
