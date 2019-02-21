# -*- coding: utf-8 -*-

""" Copy + Paste in OS X
"""


import subprocess
import os

from .base import *


def copy(string, **kwargs):
    """Copy given string into system clipboard."""
    try:
        subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE).communicate(
                string.encode("utf-8"))
    except OSError as why:
        raise XcodeNotFound

    return

def paste(**kwargs):
    """Returns system clipboard contents."""
    try:
        #Tell the IO system to decode IPC IO with utf-8,
        #to prevent UnicodeDecodeErrors on python3
        os.environ['LANG'] = 'en_US.utf-8'
        return subprocess.Popen(
            ['pbpaste'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

    except OSError as why:
        raise XcodeNotFound

