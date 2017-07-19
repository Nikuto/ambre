# ambre

## Setting the working environment
We need few tools in order to setup a proper environment, be able to build (produce the wheel file) and install the project (from a .whl file, put our sources and the dependencies in one of the PYTHONPATH variable's directory).

What's a python wheel ?
> A built-package format for Python.  
A wheel is a ZIP-format archive with a specially formatted filename and the .whl extension.  

We'll use a virtualenv to keep a clean working environment and not be annoyed by dependency issues.
>virtualenv is a tool to create isolated Python environments.  
The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into `/usr/lib/python2.7/site-packages` (or whatever your platform’s standard location is), it’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.  

Install it with `pip install virtualenv`  
A virtualenv in itself is a directory with another directory called scripts to activate this env, there is another directory lib where will be installed the different python package (the dependencies for example)  

To create a virtualenv: `virtualenv path/to/the/virtualenv`  
To activate it and gain access to the benefits of using a one:  
* *On Unix systems*: `source path/to/venv/bin/activate # or the right activation file according to your shell`  
* *On windows*: `\path\to\venv\Scripts\activate`  

Once activated every packages installed will be located in the virtualenv site-packages directory (`/venv/lib/python3.4/site-packages` for a virtualenv named venv with python3.4).  
The tool used to install external packages is pip and is shipped with python. When building the project, all the python packages needed are automatically downloaded, the external dependencies such as a C library aren't though.  
Some packages will be used to statically check the code or give the coverage of the tests, thus, type the following command to get all the required tools: `pip install -r requirements.txt`  

You should now have all the tools we'll used for the project  

## Building and installation of the project  
Our project is no different than any other dependencies we could use, it's a python package thus will be builded using wheel and installed via pip  
To build the project use: `python setup.py bdist_wheel # create a wheel in a newly appeared dist directory`  
To install it use: `pip install -U dist/ambre-0.0-py3-none-any.whl # the filename change every version`  

You should now see the installed package in your virtualenv under `/venv/lib/python3.4/site-packages/ambre/` (for a virtualenv named venv with python3.4)  

## Project architecture  
>.  
├── README.md  
├── ambre/  
│   └── tests/      
├── doc/  
├── requirements.txt  
├── setup.cfg  
└── setup.py  

All the source files composing the program should be located in `ambre`. The tests are placed in `ambre/tests`, and `doc` is the .. documentation directory. setup.cfg is for the configuration of tools used, such as flake8. setup.py is used to build the package and requirements.txt contains the list of the python tools we use (flake8, coverage..)  

## Git strategy  
* Fork
* Add the base repository as a remote: `git remote add <name> <repo_url>`. Example: `git remote add upstream https://github.com/ftsn/ambre`
* One branch per new feature: `git checkout -b <name>` to create a branch for the current one
* Never develop on master
* Write useful commit messages: describe every single sub-features your worked on
* Regularly rebase the upstream master branch to stay up to date and assure an easy integration of your work:
```bash
git fetch upstream # upstream is the name of the remote
git rebase upstream/master
```

## Code quality checking  
To ensure a high quality and a project the least buggy possible you need to follow several steps of code checking. For now this phase is composed by some unit tests using the unittest python module fired by the module coverage (whose using is pretty self explanatory) and style consistency verification through flake8  
To run the tests+coverage:  
```bash
coverage erase # to delete the previous coverage report
coverage run --source=ambre setup.py test # run the tests
coverage report # report in % the tests' coverage
```
You can generate webpage showing what's tested and what's not via the following command: `coverage html`  
Then open `htmlcov/index.html` with your favorite browser  
To run flake8: `flake8`  
The flake8's configuration is in setup.cfg, especially exclusion of useless directories during the check

