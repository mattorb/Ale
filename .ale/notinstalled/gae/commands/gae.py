#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command

from subprocess import Popen

gaefile = 'google_appengine_1.2.7.zip'
gaeversion = 'google_appengine_1.2.7'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = join(join(join(alePath('installed'), 'gae'), 'pkgs'), gaeversion)



class GaeCommand(Command):
    name = 'gae'
    shorthelp = 'run this to install gae and some helper commands to .ale'

    def execute(self, args=None):
        if args and args[0].lower() == 'start':
            p = Popen('%s/google_appengine/dev_appserver.py .' % extractPath, shell=True)
#            os.system('%s/google_appengine/dev_appserver.py .' % extractPath)
            import time
            time.sleep(2)
            Popen("open" + " http://localhost:8080", shell=True)
            sts = os.waitpid(p.pid, 0)[1]
        else:
            print 'unknown command: %s' % args[0]

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'dev_appserver.py'))
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'appcfg.py'))
        gitignore('*.pyc')
        gitignore('.DS_Store')
