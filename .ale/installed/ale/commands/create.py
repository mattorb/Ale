import os, logging

from os.path import join as join

from ale.base import Command
from ale.aleconfig import alePath

notinstalledPath = os.path.join(os.path.realpath(os.curdir), '.ale/notinstalled')
installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/installed')

class Create(Command):
    name = 'create'
    shorthelp = 'create <command> -- create the skeleton for a new command'
            
    def execute(self, args=None):
        if not args:
            logging.error('specify a command to install.')
            return
        command = args[0]
        
        os.makedirs(join(join(alePath('notinstalled'), command), 'commands'))

        init1Path = join(join(join(alePath('notinstalled'), command), '__init__.py'))
        init2Path = join(join(join(alePath('notinstalled'), command), 'commands'), '__init__.py')
        commandPath = join(join(join(alePath('notinstalled'), command), 'commands'), '%s.py' % command)
        
        initContent = """
#!/usr/bin/env python
# encoding: utf-8
"""
        
        # write the __init__.py's
        FILE = open(init1Path, 'w')
        FILE.write(initContent)
        FILE.close()

        FILE = open(init2Path, 'w')
        FILE.write(initContent)
        FILE.close()

        # write the command skeleton
        FILE = open(commandPath, 'w')
        FILE.write(
"""#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join as join
from ale.base import Command

"""
)
        FILE.write('class %sCommand(Command):\n' % command)
        FILE.write("    name = '%s'\n" % command)
        FILE.write("""
    shorthelp = 'put a short description of what the command does here'

    def execute(self, args=None):
        print 'Insert python code to do whatever the task needs to do.  Take a look at some of the other tasks (**/commands/*.py) for guidance.'
        os.system('echo echo echo echo')

## defining install is optional 
#    def install(self, args=None):
#       pass
        
""")
        FILE.close()
        
        os.system(os.environ['EDITOR'] + ' ' + commandPath)
        
        print 'Created comand: %s at %s' % (command, commandPath)
        print 'It is currently _not_ installed.  Install with "ale install <command>"'