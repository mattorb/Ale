#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from aleconfig import alePath
from utils import download, mkdir, recurse
from ale.base import Command
import shutil

finalTidyDir = join(os.path.join(alePath('recipes_installed'), 'tidy'), 'pkgs')
finalTidyPath = join(finalTidyDir, 'pythontidy.py')

class PythonTidyCommand(Command):
    name = 'tidy'
    shorthelp = 'experimental: run PythonTidy to beautify the python source files'

    def execute(self, args=None):
        def tidy(file):
            tmpFile = join(alePath('tmp'), os.path.split(file)[1] + '_tmp')
            command = finalTidyPath + ' ' + file + ' ' + tmpFile
            logging.info('Tidying %s' % (file) )
            returnCode = os.system(command)
            if returnCode == 0:
                shutil.move(tmpFile, file)
            return returnCode

        return recurse(tidy, *args)

    def install(self, args=None):
        download('http://www.lacusveris.com/PythonTidy/PythonTidy-1.16.python', 'pythontidy.py')
        mkdir(finalTidyDir)
        shutil.move(join(alePath('tmp'), 'pythontidy.py'), finalTidyPath)
        os.system('chmod +x %s' % finalTidyPath)