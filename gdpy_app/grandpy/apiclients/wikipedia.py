"""
Class Wiki:
- One method wiki_call_api() to send the request to the Wikipedia API
- Two others methods to define the parameters for the request.
get_description_page_wiki() returns description and get_url_page_wiki() returns the url
"""

import requests

class Wiki:
    """ Class to call Wiki API and search information
    corresponding to the user input """
    def __init__(self, clean_query):
        """ Initialisation """
        self.clean_query = clean_query
        self.base_url = 'https://fr.wikipedia.org/w/api.php'
        self.data = {}
        self.page_id = []

    def wiki_api_call(self, params):
        """ Send the request to the Wiki API depending on the parameters """
        req_session = requests.Session()
        req = req_session.get(url=self.base_url, params=params)
        self.data = req.json()

    def get_description_page_wiki(self):
        """ Define the parameters for the first Wiki API call,
        to get page_id and description """
        try:
            params = {
                'action':'query',
                'format':'json',
                'prop':'extracts',
                'exintro':1,
                'explaintext':1,
                'indexpageids':1,
                'generator': 'search',
                'gsrlimit':1,
                'gsrsearch': self.clean_query,
                'exsentences':3
            }

            self.wiki_api_call(params)

            # Save the page_id to get the url with get_url_page_wiki()
            self.page_id = self.data['query']['pageids']
            # Save the description as a story of GrandPy
            description = self.data['query']['pages'][self.page_id[0]]['extract']

            return self.page_id, description, True

        except KeyError:
            print('Error: ', KeyError)
            self.page_id = ['0']
            description = ""

            return self.page_id, description, False

    def get_url_page_wiki(self):
        """ Define the parameters for the second Wiki API call,
        to get the url of the wiki page """
        try:
            params = {
                'action':'query',
                'format':'json',
                'prop':'info',
                'inprop':'url',
                'pageids':self.page_id
            }

            self.wiki_api_call(params)
            if self.page_id != ['0']:
                # Save the url to propose it to the user as an in-depth look of the query
                url = self.data['query']['pages'][self.page_id[0]]['fullurl']
            else:
                url = 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'

            return url

        except KeyError:
            print('Error: ', KeyError)
