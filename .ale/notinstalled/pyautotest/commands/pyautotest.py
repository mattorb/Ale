#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command
from subprocess import Popen

extractPath = os.path.join(os.path.join(alePath('installed'), 'pyautotest'), 'pkgs')

class PyautotestCommand(Command):
    name = 'pyautotest'
    shorthelp = 'run pyautotest (continuous test runner) against the project or pyautotest [dir]'

    def execute(self, args=None):
        modipydroot = join(join(join(alePath('installed'), 'pyautotest'), 'pkgs'),'ishikawa-modipyd-4ebdf28')
        
        arg = '-v' if not args else args[0]
        
        command = join(modipydroot, "bin/pyautotest")
        print 'Executing %s %s' % (command, arg)
            
        p = Popen([command, arg], env={"PYTHONPATH": modipydroot})  #todo: just yield a generator or get all .py files
        sts = os.waitpid(p.pid, 0)[1]
        
        if sts == 0:
            print 'SUCCESS'
        else:
            print 'FAILED!'
        
    def install(self, args=None):
        dlFile = download('http://github.com/ishikawa/modipyd/zipball/release-1-0', 'ishikawa-modipyd.zip')
        extract(dlFile, extractPath)

        os.system('chmod +x %s' % join(join(join(extractPath, 'ishikawa-modipyd-4ebdf28'),'bin'), 'modipyd'))
        os.system('chmod +x %s' % join(join(join(extractPath, 'ishikawa-modipyd-4ebdf28'),'bin'), 'pyautotest'))
