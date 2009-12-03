import sys, os, re, logging

from ale.base import Command

recipes_allPath = os.path.join(os.path.realpath(os.curdir), '.ale/recipes_all')

class AvailableCommand(Command):
    name = 'search'
    shorthelp = 'search commands available for install'
    tags = 'core'
            
    def module_name_part(self, filename):
        mod_name =  filename[len(recipes_allPath) + 1:-3].replace('/', '.').replace('\\', '.')
        return re.sub('.ale.recipes_all.', '', mod_name)

    def package_name_part(self, module_name):
        return module_name.split('.')[0]
            
    def execute(self, args=None):
        files = []
        pattern = re.compile('\.ale/recipes_all.*commands/.*\.py$')

        for (dp, dn, fn) in os.walk(recipes_allPath):
            for file in fn:
                filename = os.path.join(dp, file)

                if pattern.search(filename) and not '__' in filename:
                    files.append(filename)

        modules = []
        module_names = map(self.module_name_part, files)

        if not recipes_allPath in sys.path:
            sys.path.insert(0, recipes_allPath)

        for module_name in module_names:
            logging.debug('Importing mod %s as %s' % (module_name, self.package_name_part(module_name)))
            module = __import__(module_name, globals(), locals(), [self.package_name_part(module_name)])
            modules += [module]

        from ale.base import Command
        commandList = Command.__subclasses__()

        print 'Syntax: "ale install <command>" to activate one of these\n'
        print 'Commands available for install:'

        for command in commandList:
            instance = command()
            if instance.name != 'search': # ourself is in memory when __subclassess__ was called
                if 'experimental' not in instance.tags:
                    print '   %-20.20s %s' % (instance.name, instance.shorthelp)

        print '\nCommands which are completely experimental or not working yet (under development)'

        for command in commandList:
            instance = command()
            if instance.name != 'search': # ourself is in memory when __subclassess__ was called
                if 'experimental' in instance.tags:
                    print '   %-20.20s %s' % (instance.name, instance.shorthelp)

                
        sys.path.pop()
