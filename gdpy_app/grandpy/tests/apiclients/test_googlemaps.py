"""
Test module googlemaps.py
"""
import json
import requests

from grandpy.apiclients.googlemaps import Maps

clean_query = " aquarium oceanopolis brest "
class TestMaps:
    maps = Maps(clean_query)

    def setup_method(self):
        self.clean_query = clean_query

    def test_set_up_maps_clean_query_is_ok(self):
        assert self.clean_query == self.maps.clean_query

    class MockResponse():
        def __init__(self, status_code, key_json):
            self.status_code = status_code
            self.key_json = key_json

        def mock_resp(self):
            with open("gdpy_app/grandpy/tests/apiclients/dataSet_mocks.json","r") as read_file:
                data = json.loads(read_file.read())
            for i in data[self.key_json]:
                response = i
            return response

        def json(self):
            return self.mock_resp()

    def test_call_maps_return_results_status_ok(self, monkeypatch):
        key_json = 'google_results_ok'
        response_json = TestMaps().MockResponse(200, key_json).mock_resp()

        def mock_get_coordinates_and_formatted_address(*args, **kwargs):
            return TestMaps().MockResponse(200, key_json)

        monkeypatch.setattr(requests, 'get', mock_get_coordinates_and_formatted_address)
        if response_json['status'] == 'OK':
            assert self.maps.call_maps() == (response_json['results'][0]
            	['geometry']['location']['lat'],
            	response_json['results'][0]['geometry']['location']['lng'],
            	response_json['results'][0]['formatted_address'], True)

    def test_call_maps_return_results_status_error(self, monkeypatch):
        key_json = 'google_results_error'
        response_json = TestMaps().MockResponse(400, key_json).mock_resp()
        print(response_json)

        def mock_get_coordinates_and_formatted_address(*args, **kwargs):
            return TestMaps().MockResponse(400, key_json)

        monkeypatch.setattr(requests, 'get', mock_get_coordinates_and_formatted_address)
        if response_json['status'] == 'INVALID_REQUEST':
            assert self.maps.call_maps() == (-42.1080556, 171.3361111111111,
            	"J'ai besoin de vacances...Regarde la carte, tu connais ce coin?", False)
