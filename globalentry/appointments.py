#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 autoindent smartindent:
""" globalentry.appointments

    Fetch globalentry interview appointments

>>>
>>> import globalentry
>>> globalentry.appointments.by_location_id(9300)
datetime.datetime(2020, 3, 2, 10, 45)
>>> 
>>> appts = globalentry.appointments.by_locations(['RI', 'Boston', 'VT'])
>>> len(appts)
4
>>> appts[0]
{'name': 'Warwick, RI Enrollment Center', 'id': 9300, 'next_appointment': datetime.datetime(2020, 3, 2, 10, 45)}
>>> 

"""


import globalentry


import datetime
import json
import logging
import urllib.request


SCHED_URL = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId='


def by_location_id(id):
    """ retrieve next appointment by location id
    """
    raw = urllib.request.urlopen(SCHED_URL + str(id)).read()
    appt = json.loads(raw.decode('utf-8'))
    ts = None
    if len(appt) > 0:
        ts = datetime.datetime.strptime(appt[0]['startTimestamp'], "%Y-%m-%dT%H:%M")
    return ts


def by_locations(filters):
    """ retrieve next appointments for all locations in the filter list
    """
    locs = []
    for f in filters:
        locs += globalentry.locations.filter(f)
    appts = []
    for loc in locs:
        next_appt_dt = by_location_id(loc['id'])
        appts.append({'name':loc['name'], 'id': loc['id'], 'next_appointment': next_appt_dt})
    appts.sort(key=lambda x: x['next_appointment'] or datetime.datetime.max)
    return appts


