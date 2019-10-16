# globalentry

So you went to https://ttp.cbp.dhs.gov, applied for Global Entry, paid the fee, and are now "conditionally approved". Congratulations! But you just found out that the next available interview appointment is in 6-months in a city far outside your home. You do some research only to discover longer and longer delays for these interview appointments, with year-over-year excuses. You read about this on travel websites and the recommendation is to monitor the nearest Global Entry enrollment center in case a spot becomes available. Some people in the comment section mention scripts. You are technically savvy, so here you are!

All this to avoid the long lines in passport control and customs.

## Proposed Interface

```python
>>> 
>>> import globalentry
>>> ec = globalentry.locations()
>>> len(ec)
140
>>> globalentry.next_appointment('San Diego')
datetime.datetime(2019, 3, 3, 8, 45)
>>> 
>>> 
```

## Simplify...

locations,
https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations?minimum=1&filterTimestampBy=before&timestamp=2019-11-24&serviceName=Global%20Entry
https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global Entry


next appointment,
https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId=9300


## Other Solutions

https://github.com/Drewster727/goes-notify/blob/master/goes-notify.py

