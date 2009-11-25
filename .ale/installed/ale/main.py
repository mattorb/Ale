#!/usr/bin/env python
# encoding: utf-8
import sys, os

installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/installed')

if not installedPath in sys.path:
    sys.path.insert(0, installedPath)

from ale import core

if __name__ == '__main__':
    core.Main().execute(args=sys.argv)
