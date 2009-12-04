Ale is something I got inspired to do after building [Flexvite](http://www.flexvite.com "Flexvite") on app engine.   Hopefully it saves you some time.

Requirments:  OS X 10.6, git, python 2.5 (for Appengine)

#Ale 
## Philosophy
Use only what you need, convention over configuration, but prefer dry brevity over magic, no global installs (no sudos!), bad-ass testing, best of breed tools.  Most of all, lightning fast gae python development.

## Purpose
Fair warning:  That's _still evolving_, but here's what is there now:

A command-line tool that is easy to extend (with recipes) yet keeps installed tools isolated in a project specific configuration.  

It's an odd mix of features from build tools, package management tools, and stuff you would otherwise write one-off scripts for.

There are some pre-built recipes for downloading, and configuring various tools to get your app engine python project up and 
running quickly.

It's _very_ easy to create your own recipes as well, and they're straight up python.

You can install only the tools/commands you need and remove the ones you don't.  The cool part of that is you 
(or someone new to your project) only sees the stuff that is relevant to your project (not 150 different commands 
you may or may not use).

## Install
### Option 1 - make a copy into your project
    $ mkdir myproject
    $ mkdir myproject/.ale
    $ cd myproject
    $ curl -L http://github.com/mpstx/Ale/tarball/master | tar xz --strip 1 -C .ale
    $ .ale/init.sh

### Option 2 - git submodule (your project must be have a git repo already)
The nice thing about this option is you can git pull updates of the Ale code independent of your project, at your leisure
    $ cd /myexistingproject
    $ git submodule add git://github.com/mpstx/Ale.git .ale
    $ .ale/init.sh
    
# Core Commands
## See what is installed
    $ ale
    - or - 
    $ ale list
## See what you can install
    $ ale search
    Syntax: "ale install <command>" to activate one of these

    Commands available for install:
       cleanpyc             remove *.pyc in this and all sub-dirs
       createapp            createapp [templatename]  -- create an app from a template
       gae                  google app engine .ale
       jslint               run jslint against all the .js files in the project
       pyflakes             run pyflakes (lint tool) against the project or pyflakes [dir]
       coverage             measure coverage of tests with nosetests+coverage
       test                 discover and run all unit tests using nose
       tidy                 experimental: run PythonTidy to beautify the python source files
       watcher              monitors files matching a filespec for change and triggers command(s)
    
## Install a command
    $ ale install [command]
## Remove a command you installed
    $ ale remove [command]
## Create a new command
    $ ale create [command]
## Execute a command
    $ ale [command]
    
# Jumpstarts
## Hello World - appengine local
    $ ale install gae
    $ ale install createapp
    $ ale createapp helloworldapp
    $ ale gae start

##Hello (webapp) World - appengine local
    $ ale install gae
    $ ale install createapp
    $ ale createapp helloworldwebapp
    $ ale gae start
##Linting Python files
    $ ale install pyflakes
    $ ale pyflakes
##Linting Javascript files
    $ ale install jslint
    $ ale jslint
##Unit Testing
    $ ale install test
    $ ale test
##Measuring test coverage
    $ ale install test
    $ ale coverage
##Continuous Testing
    $ ale install pyflakes
    $ ale install test
    $ ale install watcher
    $ ale watcher
    [modify a file, lint&tests re-run automatically]
    
    ... Other stuff you can do ...
    $ ale watcher add py coverage
    $ ale watcher remove py pyflakes
    
    ... Watch and trigger for multiple file types ...
    $ ale watcher add js jslint
    $ ale watcher add py coverage

    ... Create and add your own tasks to trigger ...
    $ ale create ataskyoumake
    $ ale watcher add py ataskyoumake
    $ ale watcher
    
# How to contribute
    todo....

### Sources of inspiration: homebrew, rake, pyb, paver, pykook, doit, bad experiences with globally installed libs, lack of being impressed with existing python installation/package/environment management tools -- especially in the context of appengine development