import json, requests
from DronePilot import DronePilot

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

aPilot = DronePilot()
aPilot.auth()



