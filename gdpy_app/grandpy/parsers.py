"""
Class QueryParser:
- Two methods to clean the query of the user.
normalize_query() to remove capital letters, accents and punctuation.
parser_words() to filter with stop words
"""

import re
import unicodedata

from gdpy_app.grandpy.words import STOP_WORDS, QUESTION_WORDS


class QueryParser:
    """ Class to 'clean' the user input,
    in order to detect an adress using stop words."""

    def __init__(self, user_input):
        """ Initialisation """
        self.user_input = user_input
        self.query_no_accent = ''

    def normalize_query(self):
        """ Sentence in lower case"""
        query_lower = self.user_input.lower()
        # Remove punctuation
        query_no_punctuation = re.sub(r"[!#$%&'()*+,-./:;<=>?@\^_`{|}~]+\ *", " ", query_lower)
        # Remove accent from all the words
        self.query_no_accent = ''.join((c for c in \
            unicodedata.normalize('NFD', query_no_punctuation) \
            if unicodedata.category(c) != 'Mn'))

        return query_lower, query_no_punctuation, self.query_no_accent

    def parser_words(self):
        """ Remove stop words in order to get only relevant words"""
        words = self.query_no_accent.split()
        query_words = []
        for word in words:
            if (word not in STOP_WORDS and word not in QUESTION_WORDS):
                query_words.append(word)
        query_words = ' '.join(query_words)
        return query_words
