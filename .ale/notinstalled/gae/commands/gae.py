#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import join as join
from aleconfig import *
from utils import *
from ale.base import Command

gaefile = 'google_appengine_1.2.7.zip'
gaeversion = 'google_appengine_1.2.7'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = join(join(join(alePath('installed'), 'gae'), 'pkgs'), gaeversion)

class GaeCommand(Command):
    name = 'gae'
    shorthelp = 'run this to install gae and some helper commands to .ale'

    def execute(self, args=None):
        if args and args[0].lower() == 'start':
            os.system('%s/google_appengine/dev_appserver.py .' % extractPath)
        else:
            print 'unknown command: %s' % args[0]

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        
#class ServerCommand(Command):
#    name = 'server'
#    shorthelp = 'start stop local dev_appserver for gae:  server [start/stop]'

#    def execute(self, args=None):
#        if args[0].lower() != 'start':
#            print 'Unknown app name %s' % args[0]
#            return
#            
