#!/usr/bin/env python
# encoding: utf-8
import sys
import os

# just here until we move everything up to python 2.6 or 3.0
def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for it in (item for item in seq if f(item)):
        return it

def mkdir(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

