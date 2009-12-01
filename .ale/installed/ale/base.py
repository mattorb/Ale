#!/usr/bin/env python
# encoding: utf-8

class Command(object):
    name = ''
    shorthelp = ''
    def execute(self, args):
        raise
