import re
import unicodedata

from gdpy_app.grandpy.words import STOP_WORDS, QUESTION_WORDS

 # AJOUTER EXCEPTIONS ? Et verif si userInput pas vide ?

class QueryParser:
    # """Class to 'clean' the user input, 
    # in order to detect an adress using stop words."""

    """
    >>> query = QueryParser('Hello GrandPy')
    >>> query.userInput
    'Hello GrandPy'
    """ 
    def __init__(self, userInput):
        self.userInput = userInput
        self.query_no_accent = ''
        self.query_words = []
	
    def normalize_query(self):
        # """ Sentence in lower case"""
        query_lower = self.userInput.lower()
        # """ Remove punctuation """ # .replace(',', ' ') #re..sub(r"[':,.;@#?!&$]+\ *"
        # query_no_punctuation = query_lower.translate(None,string.punctuation)
        query_no_punctuation = re.sub(r"[!#$%&'()*+,-./:;<=>?@\^_`{|}~]+\ *", " ", query_lower)

        # """ Remove accent from all the words """
        # query_encoding = unicode(query_no_punctuation,'utf-8')
        # self.query_no_accent = unicodedata.normalize('NFD', query_encoding).encode('ascii', 'ignore')
        self.query_no_accent = ''.join((c for c in unicodedata.normalize('NFD', query_no_punctuation) if unicodedata.category(c) != 'Mn'))


    # def extract_location(self):
    #     """ Try to extract a location from the user input, part of the sentence after question words"""
    #     query_location = self.query_no_accent.find()

    def parser_words(self):
        """ Remove stop words in order to get only relevant words"""
        words = self.query_no_accent.split()
        for word in words:
            if (word not in STOP_WORDS and word not in QUESTION_WORDS):
                self.query_words.append(word)
        self.query_words = ' '.join(self.query_words)
        return self.query_words

