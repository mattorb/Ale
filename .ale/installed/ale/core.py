#!/usr/bin/env python
# encoding: utf-8
import sys
import os

import logging, utils

from ale.base import Command

def importCommand(command):
    try:
        module = __import__('ale.commands.%s' % command, globals(), locals(), 'ale')
    except ImportError, e:
        logging.debug(e)
        raise e
    
    return module

def executeCommand(command, args=None):
    try:
        module = importCommand(command)
        commandInstances = [commandClass() for commandClass in Command.__subclasses__()]
        commandToExec = utils.find(lambda installedCommand: installedCommand.name == command, commandInstances)
    except ImportError, e:
        logging.error('Unknown command: %s' % command)
        return

    commandToExec.execute(args)

class Main():
    def execute(self, args=None):
        alepluginroot = os.path.dirname( os.path.realpath(__file__) )

        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s %(message)s')
        logging.debug('Running from %s' % alepluginroot)

        if args[1:]:
            executeCommand(args[1], args[2:])
        else:
            executeCommand('installed')
