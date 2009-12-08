#!/usr/bin/python
# -*- coding: utf-8 -*-

from ale.base import Command
from aleconfig import alePath
from utils import extract, gitignore, download
from os.path import join as join
import os

import logging

customStarterApps = ['xmppsendandreply','emailreceive','emailsendui']

class CreateAppCommand(Command):

    name = 'createapp'
    shorthelp = 'createapp [templatename]  -- create an app from a template'

    def execute(self, args=None):
        validTemplateNames = ['helloworld', 'helloworldwebapp', 'pale'] + customStarterApps
        if not args:
            print self.shorthelp
            print 'available app templates:'
            print 'helloworld           -- simple helloworld app'
            print 'helloworldwebapp     -- simple helloworld app using webapp fmk'
            print 'xmppsendandreply     -- simple xmpp (instant message) send and reply'
            print 'emailreceive         -- simple e-mail receive example'
            print 'emailsendui          -- simple e-mail send example'
        else:
            templateName = args[0].lower()

            if templateName not in validTemplateNames:
                print 'Unknown app name %s' % args[0]
                return
            if templateName in customStarterApps:
                tarballurl = 'http://github.com/mpstx/appengine_py_%s/tarball/master' % templateName
                tmpPath = join(join(alePath('tmp'), templateName + '.tar.gz'))
                download(tarballurl, '%s.tar.gz' % templateName)
                os.system('tar xzf %s --strip 1 -C .' % tmpPath)
            elif templateName == 'helloworld':
                logging.info('creating ./helloworld.py')
                FILE = open('./helloworld.py', 'w')
                FILE.write("""
print 'Content-Type: text/plain'
print ''
print 'Hello, world!  This is a bare bones app engine application'
""")
                FILE.close()

                logging.info('creating ./app.yaml')
                FILE = open('./app.yaml', 'w')
                FILE.write("""
application: helloworld
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: helloworld.py        
            """)
                FILE.close()
            elif templateName == 'helloworldwebapp':
                logging.info('creating ./helloworld.py')
                FILE = open('./helloworld.py', 'w')
                FILE.write("""
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
""")
                FILE.close()

                logging.info('creating ./app.yaml')
                FILE = open('./app.yaml', 'w')
                FILE.write("""
application: helloworldwebapp
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: helloworld.py        
""")
                FILE.close()
            else:
                pkgPath = join(join(alePath('recipes_installed'), 'createapp'), 'pkgs')
                templateZipPath = join(pkgPath, '%s.zip' % templateName)

                if os.path.exists(templateZipPath):
                    extract(templateZipPath, '.')
                    gitignore('tmp')
                else:
                    logging.error('Could not find template: %s' % templateName)
                    return

            return 0


