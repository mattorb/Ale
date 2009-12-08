#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

recipes_installedPath = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                         '../../recipes_installed'))

if not recipes_installedPath in sys.path:
    sys.path.insert(0, recipes_installedPath)

from ale import core

if __name__ == '__main__':
    core.Main().execute(args=sys.argv)
