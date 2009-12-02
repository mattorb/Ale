import os, logging

from ale.base import Command
import shutil
from ale.core import getCommandInstance

notinstalledPath = os.path.join(os.path.realpath(os.curdir), '.ale/notinstalled')
installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/installed')

class Install(Command):
    name = 'install'
    shorthelp = 'install <command>'
            
    def execute(self, args=None):
        if not args:
            logging.error('specify a command to install.')
            return
        command = args[0]
        sourceTree = os.path.join(notinstalledPath, command)
        destinationTree = os.path.join(installedPath, command)
        logging.info('Installing from %s to %s' % (sourceTree, destinationTree))
        shutil.copytree(sourceTree, destinationTree)
        
        instance = getCommandInstance(command)
        
        if hasattr(instance, 'install'):
            instance.install()
        
        return 0 # error count (0=success).
