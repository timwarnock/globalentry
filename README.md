# globalentry

So you went to https://ttp.cbp.dhs.gov, applied for Global Entry, paid the fee, and are now "conditionally approved". Congratulations! But you just found out that the next available interview appointment is in 6-months in a city far outside your home. You do some research only to discover longer and longer delays for these interview appointments, with year-over-year excuses. So you read about this on travel websites and the recommendation is to monitor the nearest Global Entry enrollment center in case a spot becomes available. Some people in the comment section mention scripts. You are technically savvy, so here you are!

All this to avoid the long lines in passport control and customs!


## Shell Script

```shell
$ ./find_appointments.py 
5223    : 2019-10-22 17:15:00   : Derby Line Enrollment Center
9300    : 2020-03-02 10:45:00   : Warwick, RI Enrollment Center
```

## Python Module

```python
>>> 
>>> import globalentry
>>> sites = globalentry.locations.filter('San Diego')
>>> sites[0]['id']
5002
>>> 
>>> globalentry.appointments.by_location_id(5002)
datetime.datetime(2020, 3, 3, 8, 45)
>>> 
>>> appts = globalentry.appointments.by_locations(['San Diego', 'Los Angeles'])
>>> appts[0]['next_appointment']
datetime.datetime(2019, 10, 28, 9, 15)
>>> 
```


## Other Solutions

https://github.com/Drewster727/goes-notify/blob/master/goes-notify.py

