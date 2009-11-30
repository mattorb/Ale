#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from aleconfig import *
from utils import *
from ale.base import Command

gaefile = 'google_appengine_1.2.7.zip'
gaeversion = 'google_appengine_1.2.7'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = os.path.join(alePath('installed'), gaeversion)

class GaeCommand(Command):
    name = 'gae'
    shorthelp = 'run this to install gae and some helper commands to .ale'

    def execute(self, args=None):
        print 'gae command'

    def install(self, args=None):
        mkdir(alePath('tmp'))
        localDlPath = os.path.join(alePath('tmp'), gaefile)
        curlCmd = 'curl -o %s %s' % (localDlPath, remotePath)
        print curlCmd
        os.system(curlCmd)

        mkdir(extractPath)
        os.system('unzip -d %s %s' % (extractPath, localDlPath))
        
#class ServerCommand(Command):
#    name = 'server'
#    shorthelp = 'start stop local dev_appserver for gae:  server [start/stop]'

#    def execute(self, args=None):
#        if args[0].lower() != 'start':
#            print 'Unknown app name %s' % args[0]
#            return
#            
#        if args[0].lower() == 'start':
#            system('%s/dev_appserver.sh .' % extractPath)
