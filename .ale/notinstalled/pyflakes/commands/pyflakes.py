#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from aleconfig import *
from utils import *
from ale.base import Command

class PyFlakesCommand(Command):
    name = 'pyflakes'
    shorthelp = 'run this to install gae to .ale'

    def execute(self, args=None):
        pyflakesversion = 'pyflakes-0.3.0'
        pyflakesFile = '%s.tar.gz' % pyflakesversion
        
        remotePath = '%s%s' % ('http://pypi.python.org/packages/source/p/pyflakes/', pyflakesFile)
        mkdir(alePath('tmp'))
        localDlPath = os.path.join(alePath('tmp'), pyflakesFile)
        curlCmd = 'curl -o %s %s' % (localDlPath, remotePath)
        print curlCmd
        os.system(curlCmd)

        extractPath = os.path.join(alePath('installed'), pyflakesversion)
        mkdir(extractPath)

        #todo: move the zip to the parent
        os.system('gzip -dc %s | tar xf -' % (localDlPath, extractPath))
