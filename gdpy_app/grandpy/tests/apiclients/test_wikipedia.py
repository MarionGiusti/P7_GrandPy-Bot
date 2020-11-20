import pytest 
import requests

from grandpy.apiclients.wikipedia import Wiki


clean_query = " aquarium oceanopolis brest "

class TestWiki:
    wiki = Wiki(clean_query)

    def test_set_up_wiki_clean_query_is_ok(self):
        assert self.wiki.clean_query == clean_query

    def test_get_description_page_wiki_is_ok(self, monkeypatch):
        self.data = {'batchcomplete': '', 
                     'continue': {'gsroffset': 1, 'continue': 'gsroffset||'}, 
                     'query': {'pageids': ['150231'], 
                               'pages': {'150231': {'pageid': 150231, 'ns': 0, 'title': 'Océanopolis', 'index': 1, 
                                                    'extract': "Océanopolis est un centre de culture scientifique consacré aux océans, situé à Brest, près du port de plaisance du Moulin Blanc. La forme du premier bâtiment, le pavillon tempéré, rappelle celle d'un crabe. Équipement public, Il est la propriété de Brest métropole et il est géré par une société d’économie mixte, Brest'aim."
                                                    }}}}

        self.page_id = self.data['query']['pageids']
                                            
        class MockResponse():
            def json(self):
                return self.data

        def mock_get_description_page_wiki_is_ok(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr(requests, 'get', mock_get_description_page_wiki_is_ok)
        assert self.wiki.get_description_page_wiki() == (self.data['query']['pageids'], self.data['query']['pages'][self.page_id[0]]['extract'])


    def test_get_url_page_wiki_is_ok(self, monkeypatch):
        self.data = {'batchcomplete': '', 
                     'query': {'pages': {'150231': {'pageid': 150231, 'ns': 0, 'title': 'Océanopolis', 
                     'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', 
                     'pagelanguagedir': 'ltr', 'touched': '2020-11-12T21:33:27Z', 'lastrevid': 175533769, 'length': 17458, 
                     'fullurl': 'https://fr.wikipedia.org/wiki/Oc%C3%A9anopolis', 'editurl': 'https://fr.wikipedia.org/w/index.php?title=Oc%C3%A9anopolis&action=edit', 
                     'canonicalurl': 'https://fr.wikipedia.org/wiki/Oc%C3%A9anopolis'}}}}

        self.page_id = ['150231']

        class MockResponse():        		
            def json(self):
                return self.data

        def mock_get_url_page_wiki_is_ok(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr(requests, 'get', mock_get_url_page_wiki_is_ok)
        assert self.wiki.get_url_page_wiki() == self.data['query']['pages'][self.page_id[0]]['fullurl']
