#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from aleconfig import alePath
from ale.base import Command
from subprocess import Popen

class NoseCoverageCommand(Command):
    name = 'coverage'
    shorthelp = 'measure coverage of tests with nosetests+coverage'

    def execute(self, args=None):
        prevCwd = os.getcwd()
        noseroot = join(join(join(alePath('installed'), 'test'), 'pkgs'), 'nose-0.11.0')
        coverageroot = join(join(join(alePath('installed'), 'test'), 'pkgs'), 'coverage-3.2b3')

        arg = '.' if not args else args[0]

        command = join(join(noseroot, 'bin/'), 'nosetests')
        logging.info('Executing %s %s' % (command, arg))

        pythonpath = '%s:%s' % (noseroot, coverageroot)

        p = Popen([command, '--with-coverage', '--cover-erase', '--cover-exclude-package', 'nose', arg], env={"PYTHONPATH": pythonpath})  #todo: just yield a generator or get all .py files
        sts = os.waitpid(p.pid, 0)[1]

        if sts == 0:
            print 'SUCCESS'
        else:
            print 'FAILED!'
