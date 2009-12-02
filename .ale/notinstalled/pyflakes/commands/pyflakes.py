#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from aleconfig import alePath
from utils import downloadAndExtract, recurse
from ale.base import Command
from subprocess import Popen

class PyFlakesCommand(Command):
    name = 'pyflakes'
    shorthelp = 'run pyflakes (lint tool) against the project or pyflakes [dir]'

    def execute(self, args=None):
        pyflakesroot = join(join(join(alePath('installed'), 'pyflakes'), 'pkgs'),'pyflakes-0.3.0')
        command = join(pyflakesroot, "bin/pyflakes")
        
        allSuccess = True
        
        def check(file):
            #print 'Checking %s' % file
            p = Popen([command, file], env={"PYTHONPATH": pyflakesroot})  #todo: just yield a generator or get all .py files
            sts = os.waitpid(p.pid, 0)[1]
            return sts
            
        return recurse(check, *args)
        
    def install(self, args=None):
        extractPath = os.path.join(os.path.join(alePath('installed'), 'pyflakes'), 'pkgs')
        
        downloadAndExtract('http://pypi.python.org/packages/source/p/pyflakes/pyflakes-0.3.0.tar.gz', extractPath)
