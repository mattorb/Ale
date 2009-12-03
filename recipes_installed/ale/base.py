#!/usr/bin/env python
# encoding: utf-8

class Command(object):
    name = ''
    shorthelp = ''
    tags = '' # csv list of tags
    def execute(self, args):
        raise
