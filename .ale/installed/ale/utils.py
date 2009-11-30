#!/usr/bin/env python
# encoding: utf-8
import sys
import os
from shutil import move
from aleconfig import *
import tarfile
import gzip as gzipfile

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

    if remotePath[:-7] == '.tar.gz':
        gunzip(localDlPath, localDlPath[:-3]) # extract the tar
        untar(localDlPath[:-3], extractPath)
    else:
        unzip(localDlPath, extractPath)

def untar(src=None, destdir=None):
    _src = os.path.normpath(src)
    _destdir = os.path.normpath(destdir)

    if not os.path.exists(_destdir):
        os.makedirs(_destdir)

    tarFile = tarfile.open(_src)
    prevCwd = os.getcwd()
    os.chdir(_destdir)

    for tarInfo in tarFile:
        tarFile.extract(tarInfo)
    tarFile.close()

    os.chdir(prevCwd)

def gunzip(src, destfile=None, destdir=None):
    _src = os.path.normpath(src)

    if destfile is not None:
        _destfile = os.path.normpath(destfile)
        _realdest = _destfile
        (_destdir, _destname) = os.path.split(_destfile)
    else:
        _destdir = os.path.normpath(destdir)
        (srchead, srctail) = os.path.split(_src)
        _parts = srctail.split('.')
        _newname ='.'.join(_parts[0:(len(_parts) - 1)])
        _realdest = os.path.join(_destdir, _newname)

    if not os.path.exists(_destdir):
        os.makedirs(_destdir)

    gzipFile = gzipfile.open(_src)
    destFile = open(_realdest, 'w')
    destFile.write(gzipFile.read())
    gzipFile.close()
    destFile.close()
    
def unzip(src, destdir):
    _src = os.path.normpath(src)
    _destdir = os.path.normpath(destdir)

    if not os.path.exists(_destdir):
        os.makedirs(_destdir)

    zipFile = zipfile.ZipFile(_src)
    for name in zipFile.namelist():
        path = os.path.join(_destdir, name)
        (head, tail) = os.path.split(path)
        if head and not os.path.exists(head):
            os.makedirs(head)
        destfile = open(path, 'w')
        destfile.write(zipFile.read(name))
        destfile.close()
    zipFile.close()