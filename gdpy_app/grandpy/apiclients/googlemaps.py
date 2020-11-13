import requests


class Maps:
	""" Class to interact with API GoogleMaps and collect address 
	and coordinate corresponding to the user input cleaned by the parser"""
	
	def __init__(self, clean_query):
		# Parameter clean_query is the result after the queryparser
		self.clean_query = clean_query
		self.latitude = 0
		self.longitude = 0
		self.formatted_address = 0

	def call_maps(self):
		""" Request and search coordinate from Google Maps Geocoding API"""
		base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

		# address = 'aquarium oceanopolis brest'
		address = self.clean_query

		params = {
			'key': app.config['GOOGLEMAPS_KEY'],
			'address': address
		}

		req = requests.get(base_url, params=params)
		response_json = req.json()

		if response_json['status'] == 'OK':
			geometry = response_json['results'][0]['geometry']
			self.latitude = geometry['location']['lat']
			self.longitude = geometry['location']['lng']
			self.formatted_address = response_json['results'][0] ['formatted_address']
			# return self.latitude, self.longitude, self.formatted_address

