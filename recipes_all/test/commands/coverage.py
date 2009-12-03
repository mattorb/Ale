#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from aleconfig import alePath
from ale.base import Command
from ale.core import isCommandInstalled
from subprocess import Popen
from ale.utils import relpath

def getGaeLibs():
    if isCommandInstalled('gae'):
        return [os.path.join(alePath('recipes_installed/gae/pkgs/google_appengine_1.2.7/google_appengine/'), d) for d in ('.', 'lib/django', 'lib/webob', 'lib/yaml/lib', 'lib/antlr3')]

    if os.path.exists('/usr/local/google_appine'):
        return [os.path.join('/usr/local/google_appine', d) for d in ('.', 'lib/django', 'lib/webob', 'lib/yaml/lib', 'lib/antlr3')]
    
    return []

class NoseCoverageCommand(Command):
    name = 'coverage'
    shorthelp = 'measure coverage of tests with nosetests+coverage'

    def execute(self, args=None):
        prevCwd = os.getcwd()
        noseroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'nose-0.11.0')
        coverageroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'coverage-3.2b3')

        arg = '.' if not args else args[0]

        command = join(join(noseroot, 'bin/'), 'nosetests')
        logging.info('Executing %s %s' % (relpath(command), arg))

        pythonpath = ':'.join([noseroot, coverageroot] + getGaeLibs())

        p = Popen([command, '--with-coverage', '--cover-erase', '--cover-inclusive', '--cover-exclude-package', 'nose', arg], env={"PYTHONPATH": pythonpath})
        sts = os.waitpid(p.pid, 0)[1]

        return sts
