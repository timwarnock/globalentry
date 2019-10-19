#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 autoindent smartindent:
""" globalentry.locations

    Lazy load globalentry location data

>>>
>>> import globalentry
>>> ec = globalentry.locations.list()
113
>>> 
>>> california = globalentry.locations.filter('CA')
>>> california[0]['city']
'San Diego'
>>> california[0]['id']
5002
>>> 
>>> 
>>> san_diego = globalentry.locations.by_id(5002)
>>> san_diego['address']
'2500 Paseo Internacional'
>>> 

"""


import json
import logging
import urllib.request


LOC_URL = 'https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry'
__LOCATION_LIST__ = None


def __numeric(s):
    """ guarantee a number (return 0 otherwise)
        rely on float() because the builtin isnumeric() will not handle cases like '-.5'
    """
    try:
        return float(s)
    except ValueError:
        return 0


def __get_all_locations():
    """ lazy load location data

        :filter: search string for specific locations
    """
    global __LOCATION_LIST__
    if __LOCATION_LIST__ is None:
        raw = urllib.request.urlopen(LOC_URL).read()
        __LOCATION_LIST__ = json.loads(raw.decode('utf-8'))
    return __LOCATION_LIST__


def filter(token):
    """ search through city, state, and name for matching token
    """ 
    locs = __get_all_locations()
    return [x for x in locs if token in x['name'] 
            or x['city'].startswith(token)
            or x['state'].startswith(token) ]


def by_id(id):
    """ fetch location by unique id
    """ 
    locs = __get_all_locations()
    return next((x for x in locs if x['id'] == id), None)



list = __get_all_locations

