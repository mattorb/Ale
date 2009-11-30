#!/usr/bin/env python
# encoding: utf-8
import sys, os, logging, utils, re

from ale.base import Command

aleroot = os.path.dirname( os.path.realpath(__file__) )
installedroot = os.path.realpath(os.path.join(os.path.dirname( os.path.realpath(__file__) ), '..'))

def alePath(dir):
    return os.path.join(installedroot, dir)

def findCommandFile(commandName):
    files = []
    command_file_pattern = re.compile(r'\.ale/installed.*commands/%s\.py$' % commandName.lower())

    for (dp, dn, fn) in os.walk(installedroot):
        for file in fn:
            filename = os.path.join(dp, file)
            if command_file_pattern.search(filename) and not '__' in filename:
                return filename

    raise ImportError, 'Could not locate command %s' % commandName

def importCommand(commandName):
    try:
        fullPathToCommand = findCommandFile(commandName)
        justModule = re.sub('.*installed/(?P<mod>.*)\.py$', '\g<mod>', fullPathToCommand)
        dottedModule = re.sub(r'[\\/]', '.', justModule)
        logging.debug('running %s (from %s)' % (dottedModule, fullPathToCommand))
        module = __import__(dottedModule, globals(), locals(), 'ale')
    except ImportError, e:
        logging.debug(e)
        raise e
    
    return module

def getCommandInstance(command):
    try:
        module = importCommand(command)
        commandInstances = [commandClass() for commandClass in Command.__subclasses__()]
        commandToExec = utils.find(lambda installedCommand: installedCommand.name == command, commandInstances)
    except ImportError, e:
        logging.error('Unknown command: %s' % command)
        return
    
    return commandToExec

def executeCommand(command, args=None):
    getCommandInstance(command).execute(args)

class Main():
    def execute(self, args=None):

        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s %(message)s')
        logging.debug('Running from %s' % aleroot)

        if args[1:]:
            executeCommand(args[1], args[2:])
        else:
            executeCommand('list')
