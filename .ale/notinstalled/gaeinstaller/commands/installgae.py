#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from ale.base import Command

class InstallGaeCommand(Command):
    name = 'installgae'
    shorthelp = 'run this to install gae to .ale'

    def execute(self, args=None):
        gaefile = 'google_appengine_1.2.7.zip'
        gaeversion = 'google_appengine_1.2.7'
        remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
        localDlPath = os.path.join(alePath('tmp'), gaefile)
        extractPath = os.path.join(alePath('installed/%s' % gaeversion))

        os.system('curl -o %s %s' % (localDlPath, remotePath))

        mkdir(extractPath)
        os.system('unzip -d %s %s' % (extractPath, localDlPath))
