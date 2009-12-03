#!/usr/bin/env python
# encoding: utf-8
import sys, os

recipes_installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/recipes_installed')

if not recipes_installedPath in sys.path:
    sys.path.insert(0, recipes_installedPath)

from ale import core

if __name__ == '__main__':
    core.Main().execute(args=sys.argv)
