import requests

class Wiki:
	"""docstring for Call_Wiki"""
	def __init__(self, clean_query):
		self.clean_query = clean_query
		self.base_url = 'https://fr.wikipedia.org/w/api.php'
		self.page_id = []
		self.description = ''
		self.url = ''


	def get_description_page_wiki(self):	
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

		S = requests.Session()
		R = S.get(url=self.base_url, params=params)
		data = R.json()

		self.page_id = data['query']['pageids']

		self.description = data['query']['pages'][self.page_id[0]]['extract']
		# print()
		# print(self.description)


	def get_url_page_wiki(self):
		params = {
			'action':'query',
			'format':'json',
			'prop':'info',
			'inprop':'url',
			'pageids':self.page_id
		}

		S = requests.Session()
		R = S.get(url=self.base_url, params=params)
		data = R.json()

		self.url = data['query']['pages'][self.page_id[0]]['fullurl']
		# print()
		# print(self.url)


		


		