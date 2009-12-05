#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import logging
from os.path import join as join
from utils import downloadAndExtract, gitignore
from ale.aleconfig import alePath
from ale.base import Command

from subprocess import Popen

gaefile = 'google_appengine_1.2.7.zip'
gaeversion = 'google_appengine_1.2.7'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = join(join(join(alePath('recipes_installed'), 'gae'), 'pkgs'), gaeversion)

def getAppId():
    if not os.path.exists('app.yaml'):
        logging.error('No app engine application lives here.  (no app.yaml).')
        return None
    p = re.compile('application: (.*)')
    
    appyamllines = open('app.yaml').read().split('\n')
    
    appId = None
    for line in appyamllines:
        match = p.match(line)
        if match:
            appId = match.group(1)
            break;
    
    return appId

class GaeCommand(Command):
    name = 'gae'
    shorthelp = 'google app engine .ale'

    def execute(self, args=None):
        if not args:
            print 'Syntax: ale gae [subcommand]'
            print '   Available subcommands:'
            print '   start         -- start the local dev_appserver'
            print '   deploy        -- deploy to the hosted gae app'
            print '   dash          -- open the dashboard for the hosted gae app'
            print '   logs          -- open the dashboard (on logs tab) for hosted gae app'
            print '   data          -- open the dashboard (on data tab) for hosted gae app'
            return
        
        if args and args[0].lower() == 'start':
            #--allow_skipped_files shouldn't be necesary, but don't have another work around yet...need a patch??
            p = Popen('%s/google_appengine/dev_appserver.py --allow_skipped_files .' % extractPath, shell=True)
            import time
            time.sleep(4) #todo: just do a fetch ourself to check when it has finished coming up...?
            Popen("open" + " http://localhost:8080", shell=True)
            sts = os.waitpid(p.pid, 0)[1]
        elif args and args[0].lower() == 'deploy':
            #todo: check for uncomitted changes and warn?
            os.system('%s/google_appengine/appcfg.py update .' % extractPath)
        elif args and args[0].lower() == 'dash':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/dashboard?app_id=%s' % appId)
        elif args and args[0].lower() == 'logs':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/logs?app_id=%s' % appId)
        elif args and args[0].lower() == 'data':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/datastore/explorer?app_id=%s' % appId)
        else:
            logging.error('unknown command: %s' % args[0])

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'dev_appserver.py'))
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'appcfg.py'))
        gitignore('*.pyc')
        gitignore('.DS_Store')
