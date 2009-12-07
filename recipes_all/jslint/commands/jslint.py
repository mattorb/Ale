#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import join as join
from ale.base import Command
from ale.aleconfig import alePath
from utils import downloadAndExtract, recurse, download
import shutil
import logging

finalJslintDir = join(os.path.join(alePath('recipes_installed'), 'jslint'), 'pkgs')
finalJslintPath = join(finalJslintDir, 'jslint.js')
finalRhinoJsJar = join(finalJslintDir, 'rhino1_7R2/js.jar')


class jslintCommand(Command):

    name = 'jslint'

    shorthelp = 'run jslint against all the .js files in the project'

    def execute(self, args=None):

        def jslint(file):
            tmpFile = join(alePath('tmp'), os.path.split(file)[1] + '_tmp')
            command = 'java -classpath %s org.mozilla.javascript.tools.shell.Main %s %s' % (finalRhinoJsJar,
                    finalJslintPath, file)
            logging.info('Jslint checking %s' % file)
            return os.system(command)

        return recurse(jslint, 'js', *args)

    def install(self, args=None):
        downloadAndExtract('ftp://ftp.mozilla.org/pub/mozilla.org/js/rhino1_7R2.zip', finalJslintDir)
        download('http://www.jslint.com/rhino/jslint.js', 'jslint.js')
        shutil.move(join(alePath('tmp'), 'jslint.js'), finalJslintPath)


