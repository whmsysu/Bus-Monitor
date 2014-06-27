import json
import urllib2
import time
def checkBusLoc(lineRef):
    print "Result:"
    freshRoundNum=1
    while(True):
        print freshRoundNum,":"
        url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=cfb3c75b-5a43-4e66-b7f8-14e666b0c1c1&LineRef="+lineRef
        json_input = urllib2.urlopen(url).read()
        decoded = json.loads(json_input)
        for i in range(1,len(decoded['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
)):
            print decoded['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['DirectionRef']," ",decoded['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']," ",decoded['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']        
        print "\n"
        time.sleep(10)
        freshRoundNum=freshRoundNum+1
"""
example
MTA%20NYCT_B9
"""
#lineNumber = raw_input("Line number is: ")
checkBusLoc("MTA%20NYCT_B9")
