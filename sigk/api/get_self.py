class Drone():
	def __init__(self, name= None, uuid=None, datetime=None, 
		position=None, water= None):
		self.name = name
		self.uuid = uuid
		self.datetime = datetime
		self.position = {
			'lat': 40.70, 
			'long': -74.42,
			'cog': 0.0,
			'sog':0.0 
		} if position is None else position
		self.water = {
			'temp': None,
			'dbt': None
		}
		self.history = list()
	#takes signal k json data for the drone self and constructs a Drone object.	
	def json(self, d):
		self.name = d['name']
		self.uuid = d['uuid']
		self.datetime = d['navigation']['datetime']['value']
		self.position['lat'] = d['navigation']['position']['value']['latitude']
		self.position['long'] = d['navigation']['position']['value']['longitude']
		self.position['cog'] = d['navigation']['courseOverGroundTrue']['value']
		self.position['sog'] = d['navigation']['speedOverGround']['value']
		self.water['temp'] = d['environment']['water']['temperature']['value']
		#self.water['dbt'] = d['environment']['depth']['belowTranducer']['value']

		return self
	
	#returns tuple of (lat, long)
	def getPosition(self):
		return (self.position['lat'], self.position['long'])

	#returns tuple of tuple of (lat, long) and depth below transducer	
	def getDepth(self):
		return(self.getPosition(),self.water['dbt'])

	#adds the most recent depth tuple to a history of the places the drone has been
	def setHistory(self):
		self.history.append(self.getDepth())
		return self.history