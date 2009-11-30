#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command
from subprocess import Popen

class PyFlakesCommand(Command):
    name = 'pyflakes'
    shorthelp = 'run pyflakes (lint tool) against all the python files in the project'

    def execute(self, args=None):
        prevCwd = os.getcwd()
        pyflakesroot = join(join(join(alePath('installed'), 'pyflakes'), 'pkgs'),'pyflakes-0.3.0')
        
        arg = '.' if not args else args[0]
        
        command = join(pyflakesroot, "bin/pyflakes")
        print 'Executing %s %s' % (command, arg)
            
        p = Popen([command, arg], env={"PYTHONPATH": pyflakesroot})  #todo: just yield a generator or get all .py files
        sts = os.waitpid(p.pid, 0)[1]
        
        if sts == 0:
            print 'SUCCESS'
        else:
            print 'FAILED!'
        
    def install(self, args=None):
        extractPath = os.path.join(os.path.join(alePath('installed'), 'pyflakes'), 'pkgs')
        
        downloadAndExtract('http://pypi.python.org/packages/source/p/pyflakes/pyflakes-0.3.0.tar.gz', extractPath)
