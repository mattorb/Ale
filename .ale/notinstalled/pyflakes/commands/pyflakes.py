#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from aleconfig import *
from utils import *
from ale.base import Command

class PyFlakesCommand(Command):
    name = 'pyflakes'
    shorthelp = 'run pyflakes (lint tool) against all the python files in the project'

    def execute(self, args=None):
        print 'should run pyflakes'

    def install(self, args=None):
        extractPath = os.path.join(os.path.join(alePath('installed'), 'pyflakes'), 'pkgs')
        
        downloadAndExtract('http://pypi.python.org/packages/source/p/pyflakes/pyflakes-0.3.0.tar.gz', extractPath)
