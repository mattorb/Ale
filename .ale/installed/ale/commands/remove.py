import os, logging

from ale.base import Command
import shutil

installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/installed')

class UnInstall(Command):
    name = 'remove'
    shorthelp = 'remove <command>    Uninstalls a command'
            
    def execute(self, args=None):
        if not args:
            logging.error('specify a command to uninstall.')
            return
        command = args[0]
        sourceTree = os.path.join(installedPath, command)
        logging.info('Uninstalling, deleting %s' % (sourceTree))
        if not os.path.exists(sourceTree):
            logging.error('Could not find installed command: %s' % command)
        else:
            shutil.rmtree(sourceTree)
