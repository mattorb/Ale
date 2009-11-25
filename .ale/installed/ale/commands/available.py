import sys, os, re, logging

from ale.base import Command

current_path = os.path.realpath(os.curdir)

class AvailableCommand(Command):
    name = 'available'
    shorthelp = 'list commands available for install'
            
    def module_name_part(self, filename):
        mod_name =  filename[len(current_path) + 1:-3].replace('/', '.').replace('\\', '.')
        return re.sub('.ale.notinstalled.', '', mod_name)

    def package_name_part(self, module_name):
        return module_name.split('.')[0]
            
    def execute(self):
        files = []
        pattern = re.compile('\.ale/notinstalled.*commands/.*\.py$')

        for (dp, dn, fn) in os.walk(current_path):
            for file in fn:
                filename = os.path.join(dp, file)

                if pattern.search(filename) and not '__' in filename:
                    files.append(filename)

        modules = []
        module_names = map(self.module_name_part, files)

        if not '/Volumes/subspace/ale2/.ale/notinstalled/' in sys.path:
            sys.path.insert(0, '/Volumes/subspace/ale2/.ale/notinstalled/')

        for module_name in module_names:
            logging.debug('Importing mod [%s] as %s' % (module_name, self.package_name_part(module_name)))
            module = __import__(module_name, globals(), locals(), [self.package_name_part(module_name)])
            modules += [module]

        from ale.base import Command
        commandList = Command.__subclasses__()

        for command in commandList:
            instance = command()
            if instance.name != 'available': # ourself is in memory when __subclassess__ was called
                print '%-20.20s %s' % (instance.name, instance.shorthelp)
                
        sys.path.pop()
