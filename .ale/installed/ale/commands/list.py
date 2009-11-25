import sys, os, re, logging

from ale.base import Command

installedPath = os.path.join(os.path.realpath(os.curdir), '.ale/installed')

class InstalledCommand(Command):
    name = 'list'
    shorthelp = 'list commands currently installed'
            
    def module_name_part(self, filename):
        mod_name =  filename[len(installedPath) + 1:-3].replace('/', '.').replace('\\', '.')
        return re.sub('.ale.installed.', '', mod_name)

    def package_name_part(self, module_name):
        return module_name.split('.')[0]
            
    def execute(self, args=None):
        files = []
        pattern = re.compile('\.ale/installed.*commands/.*\.py$')

        for (dp, dn, fn) in os.walk(installedPath):
            for file in fn:
                filename = os.path.join(dp, file)

                if pattern.search(filename) and not '__' in filename:
                    files.append(filename)

        modules = []
        module_names = map(self.module_name_part, files)
        for module_name in module_names:
            logging.debug('Importing mod [%s] as %s' % (module_name, self.package_name_part(module_name)))
            module = __import__(module_name, globals(), locals(), [self.package_name_part(module_name)])
            modules += [module]

        from ale.base import Command
        commandList = Command.__subclasses__()

        print 'Syntax:  ale [command]'
        print 'Available commands:'

        for command in commandList:
            instance = command()
            print '%-20.20s %s' % (instance.name, instance.shorthelp)
