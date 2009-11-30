#!/usr/bin/env python
# encoding: utf-8
import sys
import os
from shutil import move
from aleconfig import *

# just here until we move everything up to python 2.6 or 3.0
def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for it in (item for item in seq if f(item)):
        return it

def mkdir(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

def downloadAndExtract(remotePath, extractPath):
    mkdir(alePath('tmp'))
    localDlPath = os.path.join(alePath('tmp'), 'tmp.tar.gz')
    curlCmd = 'curl -o %s %s' % (localDlPath, remotePath)
    os.system(curlCmd)
    mkdir(extractPath)
    extractFile = os.path.join(extractPath, 'tmp.tar.gz')
    move(localDlPath, extractFile)
    prevCwd = os.getcwd()
    os.chdir(extractPath)
    os.system('gzip -dc %s | tar xf -' % extractFile)
    os.chdir(prevCwd)
