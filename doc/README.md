Requirments:  OS X 10.6, git, python 2.5

#Ale
## Philosophy
Use only what you need, convention over configuration, but prefer dry brevity over magic, no global installs (no sudos!), bad-ass testing, best of breed tools.  Most of all, lightning fast gae python development.

## What's the point
That's still evolving.

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