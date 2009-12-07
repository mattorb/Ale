#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

aleroot = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
recipes_installedroot = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                         '../../recipes_installed'))
recipes_allroot = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../recipes_all'))
aleapproot = os.path.dirname(os.path.realpath(__file__))


def alePath(dir):
    return os.path.join(aleroot, dir)


