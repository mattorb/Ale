#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import join as join
from aleconfig import alePath
from utils import download, recurse, mkdir
from ale.base import Command
from subprocess import Popen
import shutil

pep8root = join(os.path.join(alePath('recipes_installed'), 'pep8'), 'pkgs')
finalPep8Path = join(pep8root, 'pep8.py')


class Pep8Command(Command):

    name = 'pep8'
    shorthelp = 'run PEP8 against the project'

    def execute(self, args=None):
        command = join(pep8root, 'pep8.py')

        allSuccess = True

        def check(file):

            p = Popen([command, '--show-source', '--show-pep8', file], env={'PYTHONPATH': pep8root})
            sts = os.waitpid(p.pid, 0)[1]
            return sts

        return recurse(check, 'py', *args)

    def install(self, args=None):
        download('http://github.com/jcrocholl/pep8/raw/49fb01f94e27242c5604bbc3cb04ab7e8a593e34/pep8.py', 'pep8.py')
        mkdir(pep8root)
        shutil.move(join(alePath('tmp'), 'pep8.py'), finalPep8Path)
        os.system('chmod +x %s' % finalPep8Path)


