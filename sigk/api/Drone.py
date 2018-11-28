import json, requests

class Drone():
	def __init__(self, name= None, uuid=None, datetime=None, 
		position=None, environment= None, destination=None):
		self.name = name
		self.uuid = uuid
		self.datetime = datetime
		self.position = {
			'lat': 40.70, 
			'lng': -74.42,
			'cog': 0.0,
			'sog':0.0 
		} if position is None else position
		self.environment = {
			'temp': None,
			'dbt': None
		}
		self.destination = {
			'lat': None,
			'lng': None
		}if destination is None else destination
		self.history = list()
	#takes signal k json data for the drone self and constructs a Drone object.	
	def fromJson(self, d):
		self.name = d['name']
		self.uuid = d['uuid']
		self.datetime = d['navigation']['datetime']['value']
		self.position['lat'] = d['navigation']['position']['value']['latitude']
		self.position['lng'] = d['navigation']['position']['value']['longitude']
		self.position['cog'] = d['navigation']['courseOverGroundTrue']['value']
		self.position['sog'] = d['navigation']['speedOverGround']['value']
		self.environment['temp'] = d['environment']['water']['temperature']['value']
		#self.environment['dbt'] = d['environment']['depth']['belowTransducer']['value']

		return self
	
	#returns tuple of (lat, long)
	def getPosition(self):
		return (self.position['lat'], self.position['lng'])

	#returns tuple of tuple of (lat, long) and depth below transducer	
	def getDepth(self):
		return(self.getPosition(),self.environment['dbt'])

	#adds the most recent depth tuple to a history of the places the drone has been
	def setHistory(self):
		self.history.append({self.datetime: (self.position, self.environment)})
		return self.history

	#authenitcate device
	def auth(self):
		url = "https://vanguard-drone.local:3443/signalk/v1/api/auth/login"
		data = {"username": "drone", "password":"vanguard"}
		r = requests.post(url,json.dumps(data))
		print r 

	#PUT destination waypoint	
	def setDest(self, dest):
		self.auth()
		self.destination['lat'] = dest[0]
		self.destination['lng'] = dest[1]
		url = 'https://vanguard-drone.local:3443/signalk/v1/api/vessels/self'
		path = '/navigation/destination/value/'
		url = url + path
		#data = {'vessels': {self.uuid: {'name':self.name, 'navigation':{'destination':{'value':{'latitude':self.destination['lat'], 'longitude': self.destination['lng']}}}}},'self': self.uuid, 'version':'0.1.0'}
		data = {"value":{"latitude":self.destination['lat'], "longitude":self.destination['lng']},"source": "self"}

		print json.dumps(data,indent=4)
		r = requests.put(url, json.dumps(data), verify=False)
		return r


