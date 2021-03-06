#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
from os.path import join as join
from aleconfig import alePath
from utils import downloadAndExtract, gitignore, relpath, getGaeLibs
from ale.base import Command
from subprocess import Popen


class NosetestsCommand(Command):

    name = 'test'
    shorthelp = 'discover and run all unit tests using nose'

    def execute(self, args=None):
        prevCwd = os.getcwd()
        noseroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'nose-0.11.0')
        coverageroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'coverage-3.2b3')

        command = join(join(noseroot, 'bin/'), 'nosetests')

        args = [] if not args else args
        args += [
            '--nologcapture',
            '-m',
            'test',
            '-e',
            'lib.*',
            '-e',
            ".*\.ale.*",
            ]

        fullcommandwithargs = [command] + args
        relcommandwithargs = [relpath(command)] + args

        logging.info('Executing %s' % relcommandwithargs)

        pythonpath = ':'.join([noseroot] + getGaeLibs())

        p = Popen(fullcommandwithargs, env={'PYTHONPATH': pythonpath, 'PATH': os.environ['PATH']})  # todo: just yield a generator or get all .py files
        sts = os.waitpid(p.pid, 0)[1]

        return sts

    def install(self, args=None):
        extractPath = os.path.join(os.path.join(alePath('recipes_installed'), 'test'), 'pkgs')

        downloadAndExtract('http://python-nose.googlecode.com/files/nose-0.11.0.tar.gz', extractPath)
        downloadAndExtract('http://pypi.python.org/packages/source/c/coverage/coverage-3.2b3.tar.gz', extractPath)

        coverPyPath = join(alePath('recipes_installed/test/pkgs/nose-0.11.0/nose/plugins'), 'cover.py')
        patch1Path = join(alePath('recipes_all/test/'), 'excludecoveragepatch.patch')
        patch2Path = join(alePath('recipes_all/test/'), 'excludenosepatch.patch')

        logging.info('Patching coverage plugin...')
        os.system('patch %s %s' % (coverPyPath, patch1Path))
        os.system('patch %s %s' % (coverPyPath, patch2Path))

        logging.info('Adding to .gitignore...')
        gitignore('.coverage')
