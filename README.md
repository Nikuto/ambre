# ambre

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

