#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command
from subprocess import Popen

class ModipydCommand(Command):
    name = 'modipyd'
    shorthelp = 'run modipyd (continuous test runner) against the project or modipyd [dir]'

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
        dlFile = download('http://github.com/ishikawa/modipyd/zipball/release-1-0', 'ishikawa-modipyd.zip')
        extract(dlFile, extractPath)
