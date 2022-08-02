#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of this script/app.

Last modified in 2022-07-11

Python version 2.7.11 (Autodesk Maya 2018 and 2020)

This is the file to run from Autodesk Maya. It is advisable to create a shelf
button to run this app from there.

Important:
    Project structure:

Example:
    How a shelf button can be written::

        # -*- coding: utf-8 -*-
        u'''Maya shelf button for this app to run.

        This is a (Maya) shelf button example to make this code run without conflict
        with the Sphinx's sphinx-apidoc tool.
        '''

        import sys

        module_path = 'E:\\\\cloud\\\\Backup\\\\Libraries\\\\scripts\\\\maya\\\\python-maya-boilerplate\\\\src'

        # Includes the module path in sys.path if it is not already there:
        for path in sys.path:
            if path == module_path:
                break
        else:
            sys.path.insert(0, module_path)

        import main
        reload(main)

Note:
    If **unit tests** are in place, this is how they can be run::

        python -m unittest discover

    If coverage is being used too, this is how it can be run::

        coverage erase
        coverage run -m unittest discover
        coverage html

    In this starter kit, it is not necessary to run those commands manually,
    though. They are preconfigure in the ``package.json`` file as scripts.

Important:
    Sphinx (and its packages) **MUST** be installed in the virtual environment
    in order to avoid import errors.

    Having multiple Python versions on the machine and Sphinx installed in one
    of them, leads to confusion and hard to track bugs.

Note:
    How to generate the requirements.txt::

        pip freeze > requirements.txt

    How to install packages from requirements.txt::

        pip install -r requirements.txt

Note:
    To exclude certain modules from being documented, it is necessary to pass
    them as arguments to ``sphinx-apidoc``::

        sphinx-apidoc --force -o ./docs/sphinx/source ./src ./src/activerecord/db_credentials.py

    The example above is in the **package.json** file as the ``build:source:doc`` script.

References:
    `sphinx-apidoc ignoring some modules/packages`_

    `Coverage.py`_

    `Configuration reference`_

    `Test Code Coverage`_

    `Python Sphinx exclude patterns`_

    `sphinx-apidoc`_

    `Unpacking kwargs`_

    `PEP 484`_

    `Python docstring rendering\: reStructuredText markup inside directives not recognized`_

    `Creating the package files`_

.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
.. _Coverage.py:
   https://coverage.readthedocs.io/en/6.3.2/#coverage-py
.. _Configuration reference:
   https://coverage.readthedocs.io/en/6.3.2/config.html#configuration-reference
.. _Test Code Coverage:
   https://cpske.github.io/ISP/testing/code-coverage
.. _Python Sphinx exclude patterns:
   https://stackoverflow.com/a/43868129
.. _sphinx-apidoc:
   https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
.. _Unpacking kwargs:
   https://stackoverflow.com/a/28771348
.. _PEP 484:
   https://www.python.org/dev/peps/pep-0484/
.. _Python docstring rendering\: reStructuredText markup inside directives not recognized:
   https://youtrack.jetbrains.com/issue/PY-40010
.. _Creating the package files:
   https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files

"""

import os
import sys

import shared
import userinterface.ui_integration as ui_integration


def main():
    u"""The main function to execute the entire project/application.
    """

    # Clear the terminal window.
    os.system('cls' if os.name == 'nt' else 'clear')

    # UI CREATION
    # ==========================================================================
    global myWin  # It is very necessary!

    try:
        myWin.close()
    except:
        pass

    myWin = ui_integration.Integration()
    myWin.show()

    return "hello"


main()
