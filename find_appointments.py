#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 autoindent smartindent:
import globalentry

## set your locations
LOC = ['VT', 'Boston', 'RI']




if __name__ == "__main__":
    appts = globalentry.appointments.by_locations(LOC)
    for appt in appts:
        print(f"{appt['id']}\t: {appt['next_appointment']}\t: {appt['name']}")
