import sys, os, re, logging

from ale.base import Command

notinstalledPath = os.path.join(os.path.realpath(os.curdir), '.ale/notinstalled')

class AvailableCommand(Command):
    name = 'search'
    shorthelp = 'search commands available for install'
            
    def module_name_part(self, filename):
        mod_name =  filename[len(notinstalledPath) + 1:-3].replace('/', '.').replace('\\', '.')
        return re.sub('.ale.notinstalled.', '', mod_name)

    def package_name_part(self, module_name):
        return module_name.split('.')[0]
            
    def execute(self, args=None):
        files = []
        pattern = re.compile('\.ale/notinstalled.*commands/.*\.py$')

        for (dp, dn, fn) in os.walk(notinstalledPath):
            for file in fn:
                filename = os.path.join(dp, file)

                if pattern.search(filename) and not '__' in filename:
                    files.append(filename)

        modules = []
        module_names = map(self.module_name_part, files)

        if not notinstalledPath in sys.path:
            sys.path.insert(0, notinstalledPath)

        for module_name in module_names:
            logging.debug('Importing mod %s as %s' % (module_name, self.package_name_part(module_name)))
            module = __import__(module_name, globals(), locals(), [self.package_name_part(module_name)])
            modules += [module]

        from ale.base import Command
        commandList = Command.__subclasses__()

        print 'Commands available for install: (Install with "ale install <command>")'

        for command in commandList:
            instance = command()
            if instance.name != 'search': # ourself is in memory when __subclassess__ was called
                print '   %-20.20s %s' % (instance.name, instance.shorthelp)
                
        sys.path.pop()
