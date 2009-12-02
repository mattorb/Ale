#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from ale.base import Command
from ale.aleconfig import alePath
from ale.utils import downloadAndExtract

djangofile = 'app-engine-patch-1.1RC.zip'
djangoversion = 'app-engine-patch-1.1RC'
remotePath = '%s%s' % ('http://app-engine-patch.googlecode.com/files/', djangofile)
extractPath = join(join(join(alePath('installed'), 'django'), 'pkgs'), djangoversion)

class DjangoCommand(Command):
    name = 'django'
    tags = 'experimental'

    shorthelp = 'Experimental: django app engine patch.  Install sample project to currentdirectory -- overwrites stuff!  careful!'

    def execute(self, args=None):
        print 'Insert python code to do whatever the task needs to do.  Take a look at some of the other tasks (**/commands/*.py) for guidance.'
        os.system('echo echo echo echo')
        return 0

    def install(self, args=None):
        downloadAndExtract(remotePath, extractPath)
        os.system('mv -i %s/* .' % join(extractPath, 'app-engine-patch-sample'))
        os.system('chmod +x manage.py')
  
        
