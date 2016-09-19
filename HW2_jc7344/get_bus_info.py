from __future__ import print_function
import pylab as pl
import json
import urllib as urllib
import sys

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1] + '&VehicleMonitoringDetailLevel=calls&LineRef=' + sys.argv[2] 
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

ii = 0 
filename = sys.argv [3]
r = open(filename, 'w')
r.write('Latitude, Longitude, Stop Name, Stop Status,')
print ('Latitude, Longitude, Stop Name, Stop Status')
for i in location :
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    onwardcall = i['MonitoredVehicleJourney']['OnwardCalls']

    if len(onwardcall) is 0:
        stopname = 'N/A'
        status = 'N/A'
    else: 
        stopname = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    print (latitude,',', longitude,',', stopname,',', status)
    r.write(str(latitude) + ',' + str(longitude) + ',' + str(stopname) + ',' + str(status) + ',')
    ii = ii + 1
