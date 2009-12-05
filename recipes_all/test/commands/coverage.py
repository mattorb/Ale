#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
from os.path import join as join
from aleconfig import alePath
from ale.base import Command
from subprocess import Popen
from ale.utils import relpath, getGaeLibs

class NoseCoverageCommand(Command):
    name = 'coverage'
    shorthelp = 'measure coverage of tests with nosetests+coverage'

    def execute(self, args=None):
        prevCwd = os.getcwd()
        noseroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'nose-0.11.0')
        coverageroot = join(join(join(alePath('recipes_installed'), 'test'), 'pkgs'), 'coverage-3.2b3')

        command = join(join(noseroot, 'bin/'), 'nosetests')

        args = [] if not args else args
        args += ['--with-coverage', 
                 '--cover-erase', 
                 '--cover-inclusive', 
                 '--cover-exclude-package',  # need to generate this list somehow or find a better way to run coverage
                 'pickle,mimetypes,quopri,weakref,facebook,appengine_utilities,django,email,encodings,xml,yaml,ctypes,json,lib,codeop,hmac,sha,sgmllib,uuid,mockito,simplejson,subprocess,smtplib,uu,md5,markupbase,icalendar,hashlib,gzip,getpass,_strptime,nose,webob,urllib,google,ssl,wsgiref,urlparse,rfc822,mimetools,httplib,dummy_thread,cgi,calendar,base64,Cookie', 
                 "-m", "test", "-e", "lib.*", "-e", ".*\.ale.*"] 

        fullcommandwithargs = [command] + args
        relcommandwithargs = [relpath(command)] + args

        logging.info('Executing %s' % relcommandwithargs)

        pythonpath = ':'.join([noseroot, coverageroot] + getGaeLibs())

        p = Popen(fullcommandwithargs, env={"PYTHONPATH": pythonpath})
        sts = os.waitpid(p.pid, 0)[1]

        return sts
