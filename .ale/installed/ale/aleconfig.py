#!/usr/bin/env python
# encoding: utf-8
import sys
import os

aleroot = os.path.realpath(os.path.join(os.path.dirname( os.path.realpath(__file__) ), '../..'))
installedroot = os.path.realpath(os.path.join(os.path.dirname( os.path.realpath(__file__) ), '..'))
aleapproot = os.path.dirname( os.path.realpath(__file__))

def alePath(dir):
    return os.path.join(aleroot, dir)
