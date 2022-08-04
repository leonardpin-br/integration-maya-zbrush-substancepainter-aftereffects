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

    `closing qDialog (if exists) in pySide`_

    `PyQt and PySide Widget Best Practices`_

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
.. _closing qDialog (if exists) in pySide:
   https://stackoverflow.com/a/42600180
.. _PyQt and PySide Widget Best Practices:
   https://help.autodesk.com/view/MAYAUL/2017/CHS/?guid=__files_GUID_66ADA1FF_3E0F_469C_84C7_74CEB36D42EC_htm

"""

import os
import sys

from maya import OpenMayaUI as omui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import __version__
from shiboken2 import wrapInstance

import shared
import userinterface.ui_integration as ui_integration


def maya_main_window():
    u"""Parents this app widget under an existing Maya widget, that is, Maya's main window.

    If the widget is un-parented, it may be destroyed by the Python interpreter's garbage collector if a reference to it is not maintained.

    Returns:
        QWidget: The Maya main window.

    References:
        `Maintain a Reference to your Widget`_

        `Shiboken module`_

        `QWidget Class`_

        `QMainWindow Class`_

        `MQtUtil Class Reference`_

    .. _Maintain a Reference to your Widget:
       https://help.autodesk.com/cloudhelp/2018/ENU/Maya-SDK/files-to-wrap/GUID-66ADA1FF-3E0F-469C-84C7-74CEB36D42EC.htm
    .. _Shiboken module:
       https://doc.qt.io/qtforpython/shiboken6/shibokenmodule.html#shiboken-module
    .. _QWidget Class:
       https://doc.qt.io/qt-6/qwidget.html
    .. _QMainWindow Class:
       https://doc.qt.io/qt-6/qmainwindow.html
    .. _MQtUtil Class Reference:
       https://download.autodesk.com/us/maya/2011help/API/class_m_qt_util.html#76e5d7e2e06d5d8d6236d0ae6cad7754
    """

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)
    return mayaMainWindow


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

    myWin = ui_integration.Integration(parent=maya_main_window())
    myWin.show(dockable=True)

    return "hello"


main()
