""" globalentry - fetch locations and appointment schedule for global entry interviews """

__version__ = '0.1.0'
__author__ = 'Tim Warnock <tim@timwarnock.com>'
__all__ = ['locations', 'appointments']


import globalentry.locations
import globalentry.appointments


locations = globalentry.locations
appointments = globalentry.appointments

