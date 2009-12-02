#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from ale.base import Command

class Cleanpyc(Command):
    name = 'cleanpyc'
    shorthelp = 'remove *.pyc in this and all sub-dirs'

    def execute(self, args=None):
        command = 'find . -name *.pyc -exec rm {} \;'
        logging.info('Removing all .pyc files (Executing command: "%s")' % command)
        return os.system(command)