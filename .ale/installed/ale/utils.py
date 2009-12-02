#!/usr/bin/env python
# encoding: utf-8
import os
from aleconfig import alePath
import tarfile
import zipfile
import gzip as gzipfile
import logging

def relpath(path): # for os.path.relpath not avail until 2.6
    return path.replace(os.path.realpath(os.getcwd()), '')
    
# just here until we move everything up to python 2.6 or 3.0
def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for it in (item for item in seq if f(item)):
        return it

def mkdir(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
        
def gitignore(filePattern):
    currentIgnoredPatterns = ()
    
    if os.path.exists('.gitignore'):
        gitignoreForRead = open('.gitignore', 'r')
        currentIgnoredPatterns = set(map(str.strip, gitignoreForRead))
        gitignoreForRead.close()
    
    if not filePattern in currentIgnoredPatterns:
        logging.info('Adding pattern: [%s] to .gitignore' % filePattern)
        destFile = open('.gitignore', 'a')
        destFile.write(filePattern + '\n')
        destFile.close()

def download(remotePath, localFileNameInTmpDir=None):
    mkdir(alePath('tmp'))

    if not localFileNameInTmpDir:
        (head, tail) = os.path.split(remotePath)
        localDlPath = os.path.join(alePath('tmp'), tail)
    else:
        localDlPath = os.path.join(alePath('tmp'), localFileNameInTmpDir)
    
    logging.info('Downloading %s' % remotePath)
    
    if not os.path.exists(localDlPath):
        curlCmd = 'curl -L -o %s %s' % (localDlPath, remotePath)
        os.system(curlCmd)
    else:
        pass #we should do an MD5 check here
    
    return localDlPath

def extract(srcFile, destPath):
    if srcFile[-7:] == '.tar.gz':
        gunzip(srcFile, srcFile[:-3]) # extract the tar
        untar(srcFile[:-3], destPath)
    else:
        unzip(srcFile, destPath)

def downloadAndExtract(remotePath, extractPath):
    localDlPath = download(remotePath)
    extract(localDlPath, extractPath)

def untar(src=None, destdir=None):
    logging.info('Extracting %s to %s' % (relpath(src), relpath(destdir)))
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
    logging.info('Extracting %s to %s' % (relpath(src), relpath(destfile) if destfile else relpath(destdir)))
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
    logging.info('Extracting %s to %s' % (relpath(src), relpath(destdir)))
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
        if tail: # not there when it's just a directory
            destfile = open(path, 'w')
            destfile.write(zipFile.read(name))
            destfile.close()
    zipFile.close()
    
def dirEntries(dir_name, subdir, ignore, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)

        if not ignore(dir_name):
            if os.path.isfile(dirfile):
                if len(args) == 0:
                    fileList.append(dirfile)
                else:
                    if os.path.splitext(dirfile)[1][1:] in args:
                        fileList.append(dirfile)
            elif os.path.isdir(dirfile) and subdir:
                fileList += dirEntries(dirfile, subdir, ignore, *args)

    return fileList

def recurse(command, *args):
    errorCount = 0
    
    if not args:
        ignoreAle = lambda path : '.ale' in path
        for file in dirEntries('.', True, ignoreAle, 'py'):
            errorCount += command(file)
    else:
        pathToFile = args[0]

        if os.path.isfile(pathToFile):
            errorCount += command(pathToFile)
        else:
            ignoreAle = lambda x: not '.ale' in args[0]
            for file in dirEntries(pathToFile, True, ignoreAle, 'py'):
                errorCount += command(file)
    return errorCount
