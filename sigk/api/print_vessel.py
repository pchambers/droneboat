import json, requests
from get_self import Drone

#curl -k https://vanguard-drone.local:3443/signalk/v1/api/vessels/self/
url = 'https://vanguard-drone.local:3443/signalk/v1/api/vessels/self/'

response = requests.get(url, verify=False)

with open ("data_file.json", "w") as write_file:
	json.dump(response.json(), write_file, indent=4)

#rStr = json.dumps(response.json(), indent=4)

vessel = response.json()
 


vg1 = Drone()
vg1 = vg1.json(response.json())

print vg1.setHistory()[0]

#print response.json()
#print rStr
#print vessel['environment']['water']['temperature']