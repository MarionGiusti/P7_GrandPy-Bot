"""
Test the module parsers.py
"""
from grandpy.parsers import QueryParser

class TestQueryParser:
    # Create an instance of the class QueryParser
    query = QueryParser("Hello GrandPy! Tu sais où se trouve l'aquarium "\
     "Océanopolis à Brest?")

    def setup_method(self):
        self.user_input = "Hello GrandPy! Tu sais où se trouve l'aquarium "\
     "Océanopolis à Brest?"
        self.normalize_query = self.query.normalize_query()
        self.clean_query = self.query.parser_words()

    def test_set_up_query_userInput_attribute_is_correct(self):
        assert self.user_input == self.query.user_input

    def test_function_lower_query(self):
        assert self.normalize_query[0] == "hello grandpy! tu sais où se "\
         "trouve l'aquarium océanopolis à brest?"

    def test_function_no_punctuation(self):
        assert self.normalize_query[1] == "hello grandpy tu sais où se "\
         "trouve l aquarium océanopolis à brest "

    def test_function_no_accent(self):
        assert self.normalize_query[2] == "hello grandpy tu sais ou se "\
         "trouve l aquarium oceanopolis a brest "

    def test_the_method_parser_words_give_clean_query_with_stopwords(self):
        assert  self.clean_query == "aquarium oceanopolis brest"
