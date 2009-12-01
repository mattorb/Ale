#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from utils import downloadAndExtract, gitignore
from ale.aleconfig import alePath
from ale.base import Command

from subprocess import Popen

gaefile = 'google_appengine_1.2.7.zip'
gaeversion = 'google_appengine_1.2.7'
remotePath = '%s%s' % ('http://googleappengine.googlecode.com/files/', gaefile)
extractPath = join(join(join(alePath('installed'), 'gae'), 'pkgs'), gaeversion)

class GaeCommand(Command):
    name = 'gae'
    shorthelp = 'google app engine .ale'

    def execute(self, args=None):
        if args and args[0].lower() == 'start':
            #--allow_skipped_files shouldn't be necesary, but don't have another work around yet...need a patch??
            p = Popen('%s/google_appengine/dev_appserver.py --allow_skipped_files .' % extractPath, shell=True)
            import time
            time.sleep(4) #todo: just do a fetch ourself to check when it has finished coming up...?
            Popen("open" + " http://localhost:8080", shell=True)
            sts = os.waitpid(p.pid, 0)[1]
        elif args and args[0].lower() == 'deploy':
            #todo: check for uncomitted changes and offer to commit them
            os.system('%s/google_appengine/appcfg.py update .' % extractPath)
        else:
            if args:
                print 'unknown command: %s' % args[0]
            else:
                print 'try "ale gae start"'

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'dev_appserver.py'))
        os.system('chmod +x %s' % join(join(extractPath, 'google_appengine'), 'appcfg.py'))
        gitignore('*.pyc')
        gitignore('.DS_Store')
