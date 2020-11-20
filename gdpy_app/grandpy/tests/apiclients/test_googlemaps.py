import pytest 
import requests

from grandpy.apiclients.googlemaps import Maps

clean_query = " aquarium oceanopolis brest "

class TestMaps:
	maps = Maps(clean_query)

	def test_set_up_maps_clean_query_is_ok(self):
		assert self.maps.clean_query == clean_query

	def test_call_maps_return_results_status_ok(self, monkeypatch):

		response_json = {'results': [{
			   'address_components': [
					{'long_name': 'Port de Plaisance du Moulin Blanc', 'short_name': 'Port de Plaisance du Moulin Blanc', 'types': ['route']}, 
					{'long_name': 'Brest', 'short_name': 'Brest', 'types': ['locality', 'political']}, 
					{'long_name': 'Finistère', 'short_name': 'Finistère', 'types': ['administrative_area_level_2', 'political']}, 
					{'long_name': 'Bretagne', 'short_name': 'Bretagne', 'types': ['administrative_area_level_1', 'political']}, 
					{'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, 
					{'long_name': '29200', 'short_name': '29200', 'types': ['postal_code']}], 
				'formatted_address': 'Port de Plaisance du Moulin Blanc, 29200 Brest, France', 
				'geometry': {'location': {'lat': 48.3899736, 'lng': -4.4356012}, 
							'location_type': 'GEOMETRIC_CENTER', 
							'viewport': {'northeast': {'lat': 48.3913225802915, 'lng': -4.434252219708498}, 
										'southwest': {'lat': 48.3886246197085, 'lng': -4.436950180291502}}}, 
				'place_id': 'ChIJu6O3B4u5FkgRZqRdBjZz718', 
				'plus_code': {'compound_code': '9HQ7+XQ Brest, France', 'global_code': '8CWQ9HQ7+XQ'}, 
				'types': ['aquarium', 'establishment', 'point_of_interest', 'tourist_attraction']}], 
				'status': 'OK'}

		class MockResponse:
			def __init__(self):
				self.status_code = 200

			def json(self):
				return response_json

		def mock_get_coordinates_and_formatted_address(*args, **kwargs):
			return MockResponse()

		monkeypatch.setattr(requests, 'get', mock_get_coordinates_and_formatted_address)
		if response_json['status'] == 'OK':
			assert self.maps.call_maps() == (response_json['results'][0]['geometry']['location']['lat'], response_json['results'][0]['geometry']['location']['lng'], response_json['results'][0]['formatted_address'], True)


	def test_call_maps_return_results_status_error(self, monkeypatch):

		response_json = {'error_message': "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.", 
						 'results': [], 
				         'status': 'INVALID_REQUEST'}

		class MockResponse:	

			def __init__(self):
				self.status_code = 400	

			def json(self):
				return response_json

		def mock_get_coordinates_and_formatted_address(*args, **kwargs):
			return MockResponse()

		monkeypatch.setattr(requests, 'get', mock_get_coordinates_and_formatted_address)
		if response_json['status'] == 'INVALID_REQUEST':
			assert self.maps.call_maps() == (-42.1080556, 171.3361111111111,'', False)
