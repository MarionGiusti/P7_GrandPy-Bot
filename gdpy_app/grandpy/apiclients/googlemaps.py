"""
Class Maps:
- Has a method call_maps() to request data from the GoogleMaps API
- Returns coordinates and address
"""

import requests
from gdpy_app.website import app

class Maps:
    """ Class to request the API and collect address
    and coordinate corresponding to the user input cleaned by the parser """

    def __init__(self, clean_query):
        """ Initialisation """
        self.clean_query = clean_query

    def call_maps(self):
        """ Request and search coordinate from Google Maps Geocoding API"""
        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        address = self.clean_query
        params = {
            'key': app.config['GOOGLEMAPS_KEY'],
            'address': address
        }

        req = requests.get(base_url, params=params)
        response_json = req.json()

        respons_status = response_json['status']

        if response_json['status'] == 'OK':
            geometry = response_json['results'][0]['geometry']
            latitude = geometry['location']['lat']
            longitude = geometry['location']['lng']
            formatted_address = response_json['results'][0]['formatted_address']
            found_place = True

        else:
            print('STATUS ERROR: ', req.status_code)
            # Give coordinates and address as a dreamed destination for GrandPy
            latitude = -42.1080556
            longitude = 171.3361111111111
            formatted_address = "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"
            found_place = False

        return latitude, longitude, formatted_address, found_place, respons_status
