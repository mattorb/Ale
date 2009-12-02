#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from aleconfig import alePath
from utils import download, mkdir, dirEntries, recurse
from ale.base import Command
import shutil

finalTidyDir = join(os.path.join(alePath('installed'), 'tidy'), 'pkgs')
finalTidyPath = join(finalTidyDir, 'pythontidy.py')

class PythonTidyCommand(Command):
    name = 'tidy'
    shorthelp = 'experimental: run PythonTidy to beautify the python source files'

    def execute(self, args=None):
        def tidy(file):
            command = finalTidyPath + ' ' + file + ' ' + file
            print 'Tidying %s' % (file) 
            os.system(command) #todo: use a generator or smthng to go over all files

        recurse(tidy, *args)

    def install(self, args=None):
        download('http://www.lacusveris.com/PythonTidy/PythonTidy-1.16.python', 'pythontidy.py')
        mkdir(finalTidyDir)
        shutil.move(join(alePath('tmp'), 'pythontidy.py'), finalTidyPath)
        os.system('chmod +x %s' % finalTidyPath)