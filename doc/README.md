Requirments:  OS X 10.6, git, python 2.5, appengine

#Ale
## Philosophy
Use only what you need, convention over configuration, but prefer dry brevity over magic, no global installs (no sudos!), bad-ass testing, best of breed tools.  Most of all, lightning fast gae python development.

## What's the point
Fair warning:  That's _still evolving_, but here's what is there now:

A command-line tool that is easy to extend (with recipes) yet keeps packages isolated in a project specific configuration.  

It's an odd mix of features from build tools, package management tools, and stuff you would otherwise write a shell script for.

We have some pre-built recipes for downloading, and configuring various tools to get you app engine python project up and 
running quickly.

You can install only the tools/commands you need and remove the ones you don't.  The cool part of that is you 
(or someone new to your project) only sees the stuff that is relevant to your project (not 150 different commands 
you may or may not use).

## Install
### Option 1 - make a copy into your project
    mkdir myproject
    mkdir myproject/.ale
    cd myproject
    curl -L http://github.com/mpstx/Ale/tarball/master | tar xz --strip 1 -C .ale
    .ale/init.sh

### Option 2 - git submodule (your project must be have a git repo already)
The nice thing about this option is you can git pull updates of the Ale code independent of your project, at your leisure
    cd /myexistingproject
    git submodule add git://github.com/mpstx/Ale.git .ale
    .ale/init.sh
    
# Core Commands
## See what is installed
    ale
    - or - 
    ale list
## See what you can install
    ale search
## Install a command
    ale install [command]
## Remove a command you installed
    ale remove [command]
## Create a new command
    ale create [command]
    
# Quickstarts
## Hello World - appengine local
    ale install gae
    ale install createapp
    ale createapp helloworldapp
    ale gae start

##Hello (webapp) World - appengine local
    ale install gae
    ale install createapp
    ale createapp helloworldwebapp
    ale gae start

# How to contribute
    todo....

### Sources of inspiration:  Inspiration: homebrew, rake, pyb, paver, pykook, doit, bad experiences with globally installed libs