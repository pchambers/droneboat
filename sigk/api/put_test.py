#put_test.py

import requests, json
from DronePilot import DronePilot


pilot = DronePilot()
pilot.auth()
pilot = pilot.auth()
print pilot.authHead
print pilot.setHead(145.00).text
