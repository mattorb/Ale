#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from aleconfig import *
from utils import *
from ale.base import Command

class InstallGaeCommand(Command):
    name = 'gae'
    shorthelp = 'run this to install gae and some helper commands to .ale'

    def execute(self, args=None):
        gaefile = 'google_appengine_1.2.7.zip'
        gaeversion = 'google_appengine_1.2.7'
        remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
        mkdir(alePath('tmp'))
        localDlPath = os.path.join(alePath('tmp'), gaefile)
        curlCmd = 'curl -o %s %s' % (localDlPath, remotePath)
        print curlCmd
        os.system(curlCmd)

        extractPath = os.path.join(alePath('installed'), gaeversion)
        mkdir(extractPath)
        os.system('unzip -d %s %s' % (extractPath, localDlPath))
