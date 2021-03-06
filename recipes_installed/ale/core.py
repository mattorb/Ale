#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import logging
import utils
import re

from ale.base import Command

aleroot = os.path.dirname(os.path.realpath(__file__))
recipes_installedroot = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))


def alePath(dir):
    return os.path.join(recipes_installedroot, dir)


def findCommandFile(commandName):
    files = []
    command_file_pattern = re.compile(r'.*recipes_installed.*commands/%s\.py$' % commandName.lower())

    for (dp, dn, fn) in os.walk(recipes_installedroot):
        for file in fn:
            filename = os.path.join(dp, file)
            if command_file_pattern.search(filename) and not '__' in filename:
                return filename

    raise ImportError, 'Could not locate command %s' % commandName


def importCommand(commandName):
    try:
        fullPathToCommand = findCommandFile(commandName)
        justModule = re.sub('.*recipes_installed/(?P<mod>.*)\.py$', '\g<mod>', fullPathToCommand)
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
        commandToExec = utils.find(lambda recipes_installedCommand: recipes_installedCommand.name == command,
                                   commandInstances)
    except ImportError, e:
        logging.error('Unknown command: %s.' % command)
        print 'Search available commands with "ale search", install new command with "ale install <command>"'
        return

    return commandToExec


def isCommandInstalled(commandName):
    try:
        module = importCommand(commandName)
        return True
    except ImportError, e:
        return False


def executeCommand(command, args=None):
    instance = getCommandInstance(command)

    if instance:
        return instance.execute(args)


class Main:

    def execute(self, args=None):

        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s %(message)s')
        logging.debug('Running from %s' % aleroot)

        if args[1:]:
            result = executeCommand(args[1], args[2:])
            if result != None:
                if result > 0:
                    print 'FAILED! (%s errors)' % result
                else:
                    print 'SUCCESS'
        else:
            executeCommand('list')


