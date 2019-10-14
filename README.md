# globalentry

Are you fucking kidding me?

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
