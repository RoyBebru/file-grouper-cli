# file-grouper-cli

This is CLI variant of the File Grouper GUI application

The application is designed under Linux (Ubuntu 20.04 focal).
To be tested by virtual environment there is must be used
the following commands.

* the following command must be used only one time:

    $ pip3 install venv

* start Python's virtual environment:

    $ python3 -m venv .venv
    $ source .venv/bin/activate

* this command prevents some bad messages:

    $ .venv/bin/pip3 install wheel

* and install utility figro from the current directory "figro"

    $ .venv/bin/pip3 install .

* run figro any times you need:

    $ .venv/bin/figro -h

* and uninstall utility:

    $ .venv/bin/pip3 uninstall figro
