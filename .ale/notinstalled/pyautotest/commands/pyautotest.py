#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from aleconfig import alePath
from utils import extract, download, relpath
from ale.base import Command
from subprocess import Popen

extractPath = os.path.join(os.path.join(alePath('installed'), 'pyautotest'), 'pkgs')

class PyautotestCommand(Command):
    name = 'pyautotest'
    shorthelp = 'run pyautotest (continuous test runner) against the project or pyautotest [dir]'
    tags = 'experimental'

    def execute(self, args=None):
        modipydroot = join(join(join(alePath('installed'), 'pyautotest'), 'pkgs'),'ishikawa-modipyd-4ebdf28')
        
        arg = '.' if not args else args[0]
        
        command = join(modipydroot, "bin/pyautotest")
        logging.info('Executing %s %s' % (relpath(command), arg))
        print 'Modify a source file to trigger any dependent tests to re-execute'
            
        commandwithargs = [command, arg] if arg else [command]
            
        p = Popen(commandwithargs, env={"PYTHONPATH": '%s:%s' % (modipydroot, '.')})  #todo: just yield a generator or get all .py files
        sts = os.waitpid(p.pid, 0)[1]
        
        return sts
        
    def install(self, args=None):
        dlFile = download('http://github.com/ishikawa/modipyd/zipball/release-1-0', 'ishikawa-modipyd.zip')
        extract(dlFile, extractPath)

        os.system('chmod +x %s' % join(join(join(extractPath, 'ishikawa-modipyd-4ebdf28'),'bin'), 'modipyd'))
        os.system('chmod +x %s' % join(join(join(extractPath, 'ishikawa-modipyd-4ebdf28'),'bin'), 'pyautotest'))
