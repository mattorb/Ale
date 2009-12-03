import os, logging

from ale.base import Command
import shutil

from ale.aleconfig import recipes_installedroot

class UnInstall(Command):
    name = 'remove'
    shorthelp = 'remove <command>    Uninstalls a command'
    tags = 'core'
            
    def execute(self, args=None):
        if not args:
            logging.error('specify a command to uninstall.')
            return
        command = args[0]
        sourceTree = os.path.join(recipes_installedroot, command)
        logging.info('Uninstalling, deleting %s' % (sourceTree))
        if not os.path.exists(sourceTree):
            logging.error('Could not find recipes_installed command: %s' % command)
        else:
            shutil.rmtree(sourceTree)

        return 0
