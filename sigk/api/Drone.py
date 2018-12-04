import json, requests

class Drone():
	def __init__(self, name= None, uuid=None, datetime=None, 
		position=None, environment= None, destination=None):
		self.url = "https://vanguard-drone.local:3443/signalk/v1"
		self.sslCert = '/ssl-cert.pem'#"MIICpDCCAYwCCQCsr4J6vldnqDANBgkqhkiG9w0BAQsFADAUMRIwEAYDVQQDDAlsb2NhbGhvc3QwHhcNMTgwODI2MjAyMjIxWhcNMTkwODIxMjAyMjIxWjAUMRIwEAYDVQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDCcJre4QTvZrsz9+defh08QFxQNe4CCSvBRRc7dAeMOuCIF0ktPBqkXZXYZK02PsXJE7vPMYlbpQTinOdSVsK29TgtxvTs4V9WvO5bU2PGakl6pcqyNAfDdbHMIbZ6MnNFRm2V9tkWCE5GXEOWOlKYg6K25CEQqmZF8LMOLg8YExWdFTxLx7K4cr8L1sHiG2xmSHmwwGfwIOFugQ9lkfGagzRyqAknID0LDsZTwPorU+eSQawI4sQLui4xIy7r36an/OOTBEbx7SaUgg7rBrv3jIMgUQviJ2tDtVKn4c3wlWjVK9XkSWxFI++yOAS26LNt5Omvkwxqg9UBfbI3rBe1AgMBAAEwDQYJKoZIhvcNAQELBQADggEBALNqvxY6Ab4a1FeH5EQ8PZe+Er7IJout/zNkdIoz91skRdk/63/sKf/39P6eZ18DdMwVILKQg9hW5w8w1WNQtqrt0QBeGX+czc68MIyPHybWNcQHbgzS9Sj2SzKihxqoK19vgmoZRIIPceZJTuIFsJYc71lQUyFpuYdlmVDZoK/++VHpdbHlzSecNg/qyvO7XFFmSHQNf2c/r035ORX2KCLfPJuPq4rVZCRjuCTMVv1vwbb5VLk0sEC596SeB1usPO5JoSehAKs8jELktlSMzdDO4S6+xshzMNJwj9WOH+LpStOPmmmIIkzIfgt40EdbHRFp/xmB1yM+E5lNdyxhJfQ="
		self.sslKey = "MIIEowIBAAKCAQEAwnCa3uEE72a7M/fnXn4dPEBcUDXuAgkrwUUXO3QHjDrgiBdJLTwapF2V2GStNj7FyRO7zzGJW6UE4pznUlbCtvU4Lcb07OFfVrzuW1NjxmpJeqXKsjQHw3WxzCG2ejJzRUZtlfbZFghORlxDljpSmIOituQhEKpmRfCzDi4PGBMVnRU8S8eyuHK/C9bB4htsZkh5sMBn8CDhboEPZZHxmoM0cqgJJyA9Cw7GU8D6K1PnkkGsCOLEC7ouMSMu69+mp/zjkwRG8e0mlIIO6wa794yDIFEL4idrQ7VSp+HN8JVo1SvV5ElsRSPvsjgEtuizbeTpr5MMaoPVAX2yN6wXtQIDAQABAoIBAG5Jmr6y2a7FEYgfpD/HvuNvCi2A+Xh0JTph6xSQ8rsKplLrClm7Ds2OO7FbIZh0MJGmPNAAJA40Yrn7D4Z3qchG/U+R21kFWKOFVJm+igiAPx9vLLK5qnGmr2u+75cOSK3RjdUTB/1kRqnIKZnriO/zMncUnOCsFoizR4zSeUNIinXSbdOh8/OUJiQ8Agly/jBFw29NgVTmzj4F8mitb/HRGd3cbdC5KgAFLfov3d+VvE45QFg0zDLQJ1TuLLI28BGP9b7zukbaIliZvrtoLbSSZ+sIFWdNkj/YE0KQiLdcgHNo34Ky2O3oUWNSWo3p24Pqko8UxbCr5Ggvt5DFrp0CgYEA6ynTzLBE/mXqYYlQf5xKdKwx+nDuazmqIdJFZSkFVItq1oDwDYjjohWm97BMghKsfN9ECfxvVPBFFu/d//aab6fW9u5QM7bRs1cVgg+dafxcjWALDmrW0WAuPPwQO7NRMQOHql0+PPhvf/vwo9EkN8mxuK9nudpuaXv6nnotYQ8CgYEA06sNdRpGomgIRjPbPvpL21aIp0D4g5RW12Cl2u9ieCpBjwFl0BKE5ahXhSXV3FYWEQODaRXe96Oega6GSUF7N/KPeZnxbyhfXZjIWQ+ex/PRWo5L5VpewaSYN9TvC2JiZ2ETXREO1lh3NFud8ENuUf35gUZO5Nx5WkbSROo3MvsCgYA1NdCr1xK1cYAYM8bYKRgb0D66yUTZVEHvxzFWk3KWT7mL8b7fgSLosPeHwgd9wxXuZ2Jw1AKo+HjZmMrluPn228ZjN0dEfFB0wPan6DqZGbYjcyDtUTVsSNQNjodpyshLS94tqU2E5D3ueqZXmuIUEXo6LM5OmmMzUQ9DPqf39wKBgCRY/UicqIB/CNy1TvLznE8f/vtppsNBl+AIUrLT5L7p0rQx8z/Vzkh5rf3JT340sjldtxU2kkFIMZHnXFv8CKLE3mptSw5him7SK6VPj16audqpENNjv13VW+ZKhHoZ/PfvrZmPslKQgnfVO7vkeG9QA6Z1YlremWAtRTJcXfo9AoGBAImGmZBaI+e0XcXHPzWwsTtrzg79G5gr2fPxJkf8SLE2Xy8ahosZKPlEW+/+D6GJPUidvKbVqXCpepJ4nhcvQKtF+Tr1aKjMXJpzZr+yUn8kat8MwBcBwu63j2FRMUuQfBJddAAXmEkUY6I9Yt4AW3/N78sdlv5QQXqGtWEBBZAM"
		self.usr = 'drone'
		self.pswd = 'vanguard'
		self.auths =(self.usr, self.pswd)
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
		self.token = None

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
	#	self.environment['dbt'] = d['environment']['depth']['belowTransducer']['value']
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
"""
	#authenitcate device
	def auth(self):
		path = "/login"
		headers = {'Content-Type': 'application/json'} 
		url = self.url + path
		data = {'username': self.usr, 'password':self.pswd}
		#data = '(username=drone+password=vanguard)'
		#r = requests.post(url, data, headers = headers, verify=False)
		#print requests.post(url, data, headers = headers, verify=False)
		r = requests.put(url, headers=headers, auth=self.auths, verify=False, data=data,)
		return r
"""
	#
	def auth(self):
		url =  'https://vanguard-drone.local:3443/signalk/v1/access/requests'
		header = {"Content-Type": "application/json"}
		uuid = "1234-45653-333666"
		description = "Vanguard Drone Client"

		payload ={"clientId":"1234-45653-333666","description":"Vanguard Drone Client"}

		r = requests.post(url, json=payload, verify=False)
		print r

	#PUT destination waypoint
	def setDest(self, dest):
		#self.auth()
		self.destination['lat'] = dest[0]
		self.destination['lng'] = dest[1]
		path = '/vessels/self/navigation/destination/value/'
		url = self.url + path
		#data = {'vessels': {self.uuid: {'name':self.name, 'navigation':{'destination':{'value':{'latitude':self.destination['lat'], 'longitude': self.destination['lng']}}}}},'self': self.uuid, 'version':'0.1.0'}
		data = {"value":{"latitude":self.destination['lat'], "longitude":self.destination['lng']},"source": "self"}

		#print json.dumps(data,indent=4)
		r = requests.put(url, json.dumps(data), auth=self.auths,)
		return r

	#set active true target heading
	def setHead(self, tHead):
		#self.auth()
		path = '/vessels/self/steering/autopilot/target/headingTrue'
		url = self.url + path
		data = {"value": tHead,  "source": "actisense.204",}

		#r = requests.put(url, data, auth=self.auths, verify=False)
		r = requests.put(url, data, verify=False)
		return r

