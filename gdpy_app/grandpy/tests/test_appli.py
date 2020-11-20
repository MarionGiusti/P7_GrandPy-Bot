import pytest 
import json
import random

from gdpy_app.grandpy.words import PYBOT_ANSWER_GOOD, PYBOT_ANSWER_LOST, PYBOT_ANSWER_GET_STORY, PYBOT_ANSWER_NO_STORY

# question = "Hello GrandPy! Tu sais où se trouve l'aquarium Océanopolis à Brest?"

def test_first_answer_empty_formatted_address():
    """
    Verify the creation of a the response of gdpy.
    How with random ? It will never be  the same answer.
    Verify that the answer is the possible choice of answers ?
    """

# #     script.answer(userInput)
#     # query = QueryParser(question)
#     # queryNormalize = query.normalize_query()
#     # queryClean = query.parser_words()

#     # query_maps = googlemaps.Maps(query.query_words)
#     # query_maps.call_maps()

    formatted_address = ''

    if formatted_address == '':
        first_answer_gdpy = random.choice(PYBOT_ANSWER_LOST);
        formatted_address = "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"
    else:
        first_answer_gdpy = random.choice(PYBOT_ANSWER_GOOD);


    assert first_answer_gdpy in PYBOT_ANSWER_LOST 
    assert formatted_address == "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"

def test_first_answer_with_formatted_address():
    formatted_address = 'Port de Plaisance du Moulin Blanc, 29200 Brest, France'

    if formatted_address == '':
        first_answer_gdpy = random.choice(PYBOT_ANSWER_LOST);
        formatted_address = "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"
    else:
        first_answer_gdpy = random.choice(PYBOT_ANSWER_GOOD);

    assert first_answer_gdpy in PYBOT_ANSWER_GOOD 


def test_second_answer_empty_wiki_description():
    wiki_description = ''

    if wiki_description == '':
        second_answer_gdpy = random.choice(PYBOT_ANSWER_NO_STORY)
        wiki_description = ''
        wiki_url = ''
    else:
        second_answer_gdpy = random.choice(PYBOT_ANSWER_GET_STORY)

    assert second_answer_gdpy in PYBOT_ANSWER_NO_STORY


def test_second_answer_empty_wiki_description():
    wiki_description = 'Océanopolis est un centre de culture scientifique consacré aux océans'

    if wiki_description == '':
        second_answer_gdpy = random.choice(PYBOT_ANSWER_NO_STORY)
        wiki_description = ''
        wiki_url = ''
    else:
        second_answer_gdpy = random.choice(PYBOT_ANSWER_GET_STORY)

    assert second_answer_gdpy in PYBOT_ANSWER_GET_STORY
