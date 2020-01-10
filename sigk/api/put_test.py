#put_test.py

import requests, json
from DronePilot import DronePilot


pilot = DronePilot()
pilot = pilot.auth()
#print pilot.authHead
print pilot.setHead(145.00).text
#curl --insecure -X POST -H 'ContentType: application/json' -d '{"username" : "pi", "password" : "forecastle"}' 'https://vanguard-drone.local:3443/signalk/v1/auth/login'

#curl --insecure -X POST -H 'ContentType: application/json' -d '{"username" : "drone", "password" : "forecastle"}' 'https://vanguard-drone.local:3443/signalk/v1/api/vessels/self/steering/autopilot/target/headingTrue'
