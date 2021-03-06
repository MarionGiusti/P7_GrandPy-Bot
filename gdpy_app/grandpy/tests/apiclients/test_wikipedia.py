import os
import json
import requests
import codecs

from grandpy.apiclients.wikipedia import Wiki

class MockResponse():
    def __init__(self, key_json):
        self.key_json = key_json

    def mock_resp(self):
        with codecs.open(os.path.join(os.path.dirname(__file__))+
            "\\dataSet_mocks.json","r", encoding='utf-8') as read_file:
            data = json.loads(read_file.read())
        for i in data[self.key_json]:
            response = i
        return response

    def json(self):
        return self.mock_resp()

class TestWiki:
    def setup_method(self):
        clean_query = " aquarium oceanopolis brest "
        self.wiki = Wiki(clean_query)
        self.clean_query = clean_query

    def test_set_up_wiki_clean_query_is_ok(self):
        assert self.clean_query == self.wiki.clean_query

    def test_get_description_page_wiki_is_ok(self, monkeypatch):
        key_json = 'wiki_description_results_ok'
        response_json = MockResponse(key_json).mock_resp()
        page_id = response_json['query']['pageids']

        def mock_get_description_page_wiki_is_ok(*args, **kwargs):
            return MockResponse(key_json)

        monkeypatch.setattr(requests, 'get', mock_get_description_page_wiki_is_ok)
        if response_json['batchcomplete'] == '':
            assert self.wiki.get_description_page_wiki() == (
                response_json['query']['pageids'],
                response_json['query']['pages'][page_id[0]]['extract'], True)

    def test_get_url_page_wiki_is_ok(self, monkeypatch):
        key_json = 'wiki_url_results_ok'
        response_json = MockResponse(key_json).mock_resp()
        page_id = ['150231']
        def mock_get_url_page_wiki_is_ok(*args, **kwargs):
            return MockResponse(key_json)

        monkeypatch.setattr(requests, 'get', mock_get_url_page_wiki_is_ok)
        assert self.wiki.get_url_page_wiki(page_id) == response_json['query']['pages'][page_id[0]]['fullurl']

class TestWiki_empty:

    def setup_method(self):
        clean_query = ""
        self.wiki = Wiki(clean_query)
        self.clean_query = clean_query

    def test_set_up_wiki_clean_query_is_ok(self):
        assert self.clean_query == self.wiki.clean_query

    def test_get_description_page_wiki_not_ok(self, monkeypatch):
        key_json = 'wiki_description_results_error'
        response_json = MockResponse(key_json).mock_resp()
        page_id = ['0']

        def mock_get_description_page_wiki_not_ok(*args, **kwargs):
            return MockResponse(key_json)

        monkeypatch.setattr(requests, 'get', mock_get_description_page_wiki_not_ok)
        assert self.wiki.get_description_page_wiki() == (['0'], "", False)

    def test_get_url_page_wiki_not_ok(self, monkeypatch):
        key_json = 'wiki_url_results_error'
        response_json = MockResponse(key_json).mock_resp()
        page_id = ['0']

        def mock_get_url_page_wiki_not_ok(*args, **kwargs):
            return MockResponse(key_json)

        monkeypatch.setattr(requests, 'get', mock_get_url_page_wiki_not_ok)
        assert self.wiki.get_url_page_wiki(page_id) == 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'
