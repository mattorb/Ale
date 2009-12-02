#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from ale.base import Command
from ale.core import executeCommand
from ale.utils import dirEntries
import logging
import time

class WatcherCommand(Command):
    name = 'watcher'
    shorthelp = 'monitors files matching a filespec for change and triggers command(s)'
    
    watchlist = {'py':['pyflakes', 'test']}

    def notify(self, success):
        if success:
            pass
        else:
            print '************************ERROR.  You need to fix this.  ********************************'

    def execute(self, args=None):
        ignoreAle = lambda path : '.ale' in path
        
        filesForType = {}
        for type in self.watchlist.iterkeys():
            filesForType[type] = dirEntries('.', True, ignoreAle, type)

        def getLastTouch(files):
            lasttouch = 0.0
            for file in files:
                if os.path.getmtime(file) > lasttouch:
                    lasttouch = os.path.getmtime(file)
            return lasttouch

        logging.info('Watcher started.')
        
        for type in self.watchlist.iterkeys():
            for command in self.watchlist[type]:
                logging.info('When *.%s changes, execute %s' % (type, command))

        for type in self.watchlist.iterkeys():
            logging.info('Monitoring %s .%s files for changes...' % (len(filesForType[type]), type))

        currenttouch = 0.0
        
        while True:
            for type in self.watchlist.iterkeys():
                snapshotTouch = getLastTouch(filesForType[type])
                if snapshotTouch > currenttouch:
                    for command in self.watchlist[type]:
                        result = executeCommand(command, [])
                        self.notify(result == 0)

                    currenttouch=snapshotTouch
                time.sleep(1)

        return 0 # error count (0=success).
        
#    def addWatch(fileextension, command):
        # verify the command is installed.
        # add the watch
        # store the watch list
#        pass
        
#    def removeWatch(fileextension, command):
        # remove the watch
        # store the watch list
#        pass