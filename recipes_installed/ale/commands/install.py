#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging

from ale.base import Command
import shutil
from ale.core import getCommandInstance
from ale.utils import relpath
from ale.aleconfig import recipes_installedroot, recipes_allroot


class Install(Command):

    name = 'install'
    shorthelp = 'install <command>'
    tags = 'core'

    def execute(self, args=None):
        if not args:
            logging.error('specify a command to install.')
            return
        command = args[0]
        sourceTree = os.path.join(recipes_allroot, command)
        destinationTree = os.path.join(recipes_installedroot, command)
        logging.info('Installing from %s to %s' % (relpath(sourceTree), relpath(destinationTree)))

        if os.path.exists(destinationTree):
            logging.error('%s is already recipes_installed.   To re-install, "ale remove %s" first. ' % (command,
                          command))
            return 1

        shutil.copytree(sourceTree, destinationTree)

        instance = getCommandInstance(command)

        if hasattr(instance, 'install'):
            instance.install()

        return 0  # error count (0=success).


