#!/usr/bin/env python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 autoindent smartindent:
import globalentry
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Look for Global Entry interview appointments')
    parser.add_argument('locations', metavar='LOC', type=str, nargs='+', help='locations to search for')
    args = parser.parse_args()
    appts = globalentry.appointments.by_locations(args.locations)
    for appt in appts:
        print(f"{appt['next_appointment']}\t: {appt['name']} ({appt['id']})")

