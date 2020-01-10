#DronePilot.py
import requests, json

class DronePilot():
	def __init__(self):
		self.root = 'https://vanguard-drone.local:3443/signalk/v1'
		self.uuid = '1234-45653-333666'
		self.source = "VanguardPilot.AI"
		self.token = None
		self.authHead ={}
		
	#setup authorization of device:
	def auth(self):
		path =  '/access/requests'
		url = self.root + path
		description = "Vanguard Drone Pilot Client"
		payload ={"clientId":self.uuid,"description":description}

		try:
			#tesat to see if auth has already None
			#print "call testReg"
			self.token = testReg("auth_resp.json")	
			self.authHead = {'Authorization':'token %s' % self.token}
		except:	
			#if not start 
			print "Exception, auth not processed"
			r = requests.post(url, json=payload, verify=False)
			saveJson(r, "auth_resp")
			#print "first request"
		return self
#----------------- Working Functions -------------------------------
	"""
	#PUT destination waypoint
	def setDest(self, dest):
		#self.auth()
		self.destination['lat'] = dest[0]
		self.destination['lng'] = dest[1]
		path = '/vessels/self/navigation/destination/value/'
		url = self.root + path
		#data = {'vessels': {self.uuid: {'name':self.name, 'navigation':{'destination':{'value':{'latitude':self.destination['lat'], 'longitude': self.destination['lng']}}}}},'self': self.uuid, 'version':'0.1.0'}
		data = {"value":{"latitude":self.destination['lat'], "longitude":self.destination['lng']},"source": "self"}

		#print json.dumps(data,indent=4)
		r = requests.put(url, json.dumps(data), auth=self.auths,)
		return r
	"""
	#set active true target heading
	def setHead(self, tHead):
		#self.auth()
		path = '/vessels/self/steering/autopilot/target/headingTrue'
		url = self.root + path
		data = {"value": tHead,  "source": self.source}
		header = self.authHead	
		header["Content-Type"] = "applications/json"
		#r = requests.put(url, data, auth=self.auths, verify=False)
		r = requests.put(url, json=data, verify=False, headers=header)
		return r 	

#----------------- HELPERS -------------------------------
#test a local .json file to see if there is already a token saved, and if the local 
def testReg(fn):
	try:
		#print "read token.json"
		with open("token.json", "r") as token_read:
			td= json.load(token_read)	
		token = td["accessRequest"]["token"]
		#print "Token: "
		#print token
		#token = findKey(td)

	except:
		#print "searching auth_resp.json"
		with open ("auth_resp.json", "r") as json_data:
			d = json.load(json_data)
		
		path = d["href"] 
		url = "https://vanguard-drone.local:3443" + path
		#print url
		r = requests.get(url, verify=False)
		
		if r.json()["state"]=="DENIED":
			print "Error with login"
		if r.json()["state"]=="PENDING":
			print "Verification pending on server console"
		elif r.json()["state"]=="COMPLETED":
			saveJson(r, "token")
			token = r.json()["accessRequest"]["token"]
			#token = findKey(r.json())
			#print "just saved token"

	return token

#search for the authKey in a json file
def findKey(response):
	#print response
	if response['accessRequest']['permission'] == 'APPROVED':
		return response['accessRequest']['token']

#save the json object r as filename name
def saveJson(r,name):
	fn = name +".json"
	with open (fn, "w") as write_file:
		json.dump(r.json(), write_file, indent=4)
	return fn



