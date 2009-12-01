#!/usr/bin/python
# -*- coding: utf-8 -*-
from ale.base import Command
import logging

class CreateAppCommand(Command):
    name = 'createapp'
    shorthelp = 'createapp [templatename]  -- create the gae hello world app in the current directory from template'

    def execute(self, args=None):
        if not args:
            print self.shorthelp
            print 'available app templates:'
            print 'helloworld'
            print 'helloworldwebapp'
        else:
            if args[0].lower() != 'helloworld' and args[0].lower() != 'helloworldwebapp':
                print 'Unknown app name %s' % args[0]
                return
            
            if args[0].lower() == 'helloworld':
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
            elif args[0].lower() == 'helloworldwebapp':
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
            logging.info('SUCCESS')
