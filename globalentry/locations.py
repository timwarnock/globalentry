#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 autoindent smartindent:
""" 

>>>
>>>
>>>
"""
import logging
import urllib.request


def __numeric(s):
    """ guarantee a number (return 0 otherwise)
        rely on float() because the builtin isnumeric() will not handle cases like '-.5'
    """
    try:
        return float(s)
    except ValueError:
        return 0


def __get():
    """ 
    """
    raw_html = urllib.request.urlopen("http://example.com/api").read()
    return raw_html

