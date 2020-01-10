import json, requests
from Drone import Drone

#curl -k https://vanguard-drone.local:3443/signalk/v1/api/vessels/self/
url = 'https://vanguard-drone.local:3443/signalk/v1/api/vessels/self/'

response = requests.get(url, verify=False)

with open ("data_file.json", "w") as write_file:
	json.dump(response.json(), write_file, indent=4)

#rStr = json.dumps(response.json(), indent=4)
 
vg1 = Drone()
vg1 = vg1.fromJson()#response.json())
print	vg1.name	
print vg1.getDepth()


#print vg1.setHistory()[0]

#r1= vg1.auth() 
#print r1.request.url
#print r1


#r2 = vg1.setHead(150.00)
#print r2.request.url	
#print r2


#print response.json()
#print rStr
#print vessel['environment']['water']['temperature']