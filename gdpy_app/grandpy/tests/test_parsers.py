import grandpy.parsers as script
import pytest 

# def hello(name):
#     return 'Hello ' + name

# def test_hello():
#     assert hello('Marion') == 'Hello Marion'

# Créer instance classe Parser
class TestQueryParser:
	
	def setup_method(self):
		query = script.QueryParser("Hello GrandPy ! Tu sais où se trouve l'aquarium Océanopolis à Brest ?")
		assert query.userInput == "Hello GrandPy ! Tu sais où se trouve l'aquarium Océanopolis à Brest ?"

		assert query.userInput.lower() == "hello grandpy ! tu sais où se trouve l'aquarium océanopolis à brest ?"

	# def test_normalize_query(self):
	# 	query_lower = query.userInput.lower()
	# 	assert query_lower == "hello grandpy ! tu sais où se trouve l'aquarium océanopolis à brest ?"

	# - Récupérer saisie utilisateur
	# def test_normalize_query():
	# 	query.userInput = "ola"
	# 	assert quer.userInput == "ola"

