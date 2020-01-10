import json, requests
from DronePilot import DronePilot
from Drone import Drone

#https://github.com/SignalK/specification/blob/put-message-fix/gitbook-docs/access_requests.md
#


"""
curl -k \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"clientId":"1234-45653-343453","description":"My Awesome Humidity Sensor"}' \
    https://localhost:3443/signalk/v1/access/requests

url =  'https://vanguard-drone.local:3443/signalk/v1/access/requests'
header = {"Content-Type": "application/json"}
uuid = "1234-45653-333666"
description = "Vanguard Drone Client"

payload ={"clientId":"1234-45653-333666","description":"Vanguard Drone Client"}
r = requests.post(url, json=payload, verify=False)
"""

vg1 = Drone()
#vg1.fromJson()
#print vg1.getDepth()
#print vg1.getPosition()
#print "attempting to set heading"
#print vg1.setHead(145.00).text

"""
#failed test
aUrl = vg1.url + '/api/vessels/' + vg1.RegExp + '/navigation/position'
r = requests.get(aUrl, auth=('drone','vanguard'))
print "auths"
print r
"""

#print vg1.auth2()
#print vg1.token

s = requests.Session()
payload = vg1.login
head = {'Content-Type': 'application/json'}
url = vg1.url + '/auth/login'
r = s.post(url, json=payload, headers=head, verify=False)
vg1.token = r.json()['token']

print 'token request'
print r
vg1.token = r.json()['token']

testUrl = vg1.url + '/auth/loginStatus'
print s.get(testUrl,verify=False)

## Test put
path = '/vessels/self/steering/autopilot/target/headingTrue'
url = vg1.url + path
header = {'Authorization':vg1.token, 'Content-Type':'application/json'}
payload = {"value": 145.00,	"source": "Vanguard Pilot",	}
#r = s.put(url, json=payload, headers=header, verify=False)
print 'put heading request'
print r
