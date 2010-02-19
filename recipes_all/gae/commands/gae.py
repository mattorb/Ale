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

gaefile = 'google_appengine_1.3.1.zip'
gaeversion = 'google_appengine_1.3.1'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = join(join(join(alePath('recipes_installed'), 'gae'), 'pkgs'), gaeversion)

class NoApplicationFoundNoAppYamlHere(Exception):
    pass

def getAppId():
    if not os.path.exists('app.yaml'):
        logging.error('No app engine application lives here.  (no app.yaml).')
        raise NoApplicationFoundNoAppYamlHere

    p = re.compile('application: (.*)')

    appyamllines = open('app.yaml').read().split('\n')

    appId = None
    for line in appyamllines:
        match = p.match(line)
        if match:
            appId = match.group(1)
            break

    return appId


class GaeCommand(Command):

    name = 'gae'
    shorthelp = 'google app engine .ale'

    def execute(self, args=None):
        if not args:
            print 'Syntax: ale gae [subcommand]'
            print '   Available subcommands:'
            print '   start         -- start the local dev_appserver and launch browser'
            print '   deploy        -- deploy to the hosted gae app and launch browser'
            print '   dash          -- open the dashboard for the hosted gae app'
            print '   log           -- open the dashboard (on logs tab) for hosted gae app'
            print '   data          -- open the dashboard (on data tab) for hosted gae app'
            print '   doc           -- open the gae python docs'
            print '   remoteshell   -- open a shell to the remote, deployed app'
            return

        if args and args[0].lower() == 'start':

            p = Popen('%s/google_appengine/dev_appserver.py --allow_skipped_files .' % extractPath, shell=True)
            import time
            time.sleep(4)  # todo: just do a fetch ourself to check when it has finished coming up...?
            Popen('open' + ' http://localhost:8080', shell=True)
            sts = os.waitpid(p.pid, 0)[1]
        elif args and args[0].lower() == 'deploy':
            appId = getAppId()
            os.system('%s/google_appengine/appcfg.py update .' % extractPath)
            os.system('open http://%s.appspot.com' % appId)
        elif args and args[0].lower() == 'dash':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/dashboard?app_id=%s' % appId)
        elif args and args[0].lower() == 'log':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/logs?app_id=%s' % appId)
        elif args and args[0].lower() == 'data':
            appId = getAppId()
            if appId:
                os.system('open http://appengine.google.com/datastore/explorer?app_id=%s' % appId)
        elif args and args[0].lower() == 'doc':
            os.system('open http://code.google.com/appengine/docs/python/')
        elif args and args[0].lower() == 'remoteshell':
            appId = getAppId()
            logging.info("Starting remoteshell for app: %s.  Careful you are working against your _live_ deployed app! " % appId)
            fullcommandwithargs = ['python', alePath("recipes_installed/gae/pkgs/google_appengine_1.3.1/google_appengine/") + 'remote_api_shell.py', appId]

            p = Popen(fullcommandwithargs, env={'PYTHONPATH': os.environ['PYTHONPATH'] + ':lib:.', 'PATH': os.environ['PATH']})  # todo: just yield a generator or get all .py files
            sts = os.waitpid(p.pid, 0)[1]

        else:
            logging.error('unknown command: %s' % args[0])

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'dev_appserver.py'))
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'appcfg.py'))
        gitignore('*.pyc')
        gitignore('.DS_Store')


