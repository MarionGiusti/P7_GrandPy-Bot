import pytest 
import re
import unicodedata

from grandpy.parsers import QueryParser
from grandpy.words import STOP_WORDS, QUESTION_WORDS

userInput = "Hello GrandPy! Tu sais où se trouve l'aquarium Océanopolis à Brest?"

class TestQueryParser:
	# Create an instance of the class QueryParser
    query = QueryParser(userInput)

    def test_set_up_query_userInput_attribute_is_correct(self):
        assert self.query.userInput == userInput

    def test_function_lower_query(self):
        query_lower = self.query.userInput.lower()
        assert query_lower == "hello grandpy! tu sais où se trouve l'aquarium océanopolis à brest?"

    def test_function_no_punctuation(self):
        query_lower = "hello grandpy! tu sais où se trouve l'aquarium océanopolis à brest?"
        query_no_punctuation = re.sub(r"[!#$%&'()*+,-./:;<=>?@\^_`{|}~]+\ *", " ", query_lower)
        assert query_no_punctuation == "hello grandpy tu sais où se trouve l aquarium océanopolis à brest "

    def test_function_no_accent(self):
        query_no_punctuation = "hello grandpy tu sais où se trouve l aquarium océanopolis à brest "
        query_no_accent = ''.join((c for c in unicodedata.normalize('NFD', query_no_punctuation) if unicodedata.category(c) != 'Mn'))
        assert query_no_accent == "hello grandpy tu sais ou se trouve l aquarium oceanopolis a brest "

    #     self.query.query_no_accent = ''.join((c for c in unicodedata.normalize('NFD', query_no_punctuation) if unicodedata.category(c) != 'Mn'))
    #     assert self.query.query_no_accent == "hello grandpy tu sais ou se trouve l aquarium oceanopolis a brest "

    def test_the_method_normalize_query_minimize_letter_delete_accent_punctuation(self):
        self.query.normalize_query()
        assert self.query.query_no_accent  == "hello grandpy tu sais ou se trouve l aquarium oceanopolis a brest "


    def test_the_method_parser_words_give_clean_query_with_stopwords(self):
        self.query.parser_words()
        assert self.query.query_words == "aquarium oceanopolis brest"

