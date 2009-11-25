#!/usr/bin/python
# -*- coding: utf-8 -*-
from ale.base import Command
import logging

class CreateAppCommand(Command):
    name = 'createapp'
    shorthelp = 'create the gae hello world app in the current directory from template'

    def execute(self, args=None):
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
        
        logging.info('All Done!   Run "dev_appserver ." to start the local server, then browser to http://localhost:8080')