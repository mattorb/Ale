#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from ale.base import Command
from aleconfig import alePath
from utils import extract, download, relpath, getGaeLibs
from subprocess import Popen

extractPath = os.path.join(os.path.join(alePath('recipes_installed'), 'shell'), 'pkgs')

class ShellCommand(Command):
    name = 'shell'

    shorthelp = 'Launch iPython (local) shell with the proper python path'

    def execute(self, args=None):
        ipythonroot = join(join(join(alePath('recipes_installed'), 'shell'), 'pkgs'), 'ipython-0.10')

        command = join(ipythonroot, 'ipython.py')
        logging.info('%s' % command)

        logging.info('Executing %s %s' % (relpath(command), args))

        commandwithargs = [command] + args if args else [command]
        
        commandwithargs += ['-ipythondir', join(ipythonroot, 'UserConfig')]
        commandwithargs += ['-color_info']

        pythonpath = ':'.join(['.'] + ['lib'] + getGaeLibs())

        p = Popen(commandwithargs, env={'PATH':os.environ['PATH'], 'PYTHONPATH': pythonpath, 'HOME': os.environ['HOME']})
        sts = os.waitpid(p.pid, 0)[1]

        return sts

    def install(self, args=None):
        dlFile = download('http://ipython.scipy.org/dist/ipython-0.10.tar.gz', 'ipython-0.10.tar.gz')
        extract(dlFile, extractPath)
        
