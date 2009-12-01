#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from ale.base import Command

class Cleanpyc(Command):
    name = 'cleanpyc'
    shorthelp = 'remove *.pyc in this and all sub-dirs'

    def execute(self, args=None):
        command = 'find . -name *.pyc -exec rm {} \;'
        print 'Removing all .pyc files (Executing command: "%s")' % command
        os.system(command)