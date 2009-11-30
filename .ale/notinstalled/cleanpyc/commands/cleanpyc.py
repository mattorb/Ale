#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command
from subprocess import Popen

class Cleanpyc(Command):
    name = 'cleanpyc'
    shorthelp = 'remove *.pyc in this and all sub-dirs'

    def execute(self, args=None):
        command = 'find . -name *.pyc -exec rm {} \;'
        print 'Removing all .pyc files (Executing command: "%s")' % command
        os.system(command)