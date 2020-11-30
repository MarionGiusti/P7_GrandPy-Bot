"""
Module with main function answer() which creates instances of the
QueryParser, Maps and Wiki Classes.
Create random answer of GrandPy Bot.
"""
import random

from gdpy_app.grandpy.apiclients.googlemaps import Maps
from gdpy_app.grandpy.apiclients.wikipedia import Wiki
from gdpy_app.grandpy.parsers import QueryParser
from gdpy_app.grandpy.words import PYBOT_ANSWER_GOOD, PYBOT_ANSWER_LOST
from gdpy_app.grandpy.words import PYBOT_ANSWER_GET_STORY, PYBOT_ANSWER_NO_STORY

def analyse_question(question):
    """ Analyse the user's question """
    query = QueryParser(question)
    query.normalize_query()
    query_clean = query.parser_words()
    return query_clean

def data_apis(query_clean):
    """ Request GoogleMaps API and MediaWiki API """
    # Get an address and coordinates
    query_maps = Maps(query_clean)
    result_maps = query_maps.call_maps()
    # Get the first lines from an article corresponding to the queryClean
    query_wiki = Wiki(query_clean)
    result_description = query_wiki.get_description_page_wiki()
    result_url = query_wiki.get_url_page_wiki(result_description[0])

    return result_maps, result_description, result_url

def create_first_answer(result_maps):
    """ Get first answer of Grandpy depending on the results of the GoogleMaps API
    request returned """
    if result_maps[3]:
    # Found a place
        first_answer_gdpy = random.choice(PYBOT_ANSWER_GOOD)
    else:
        first_answer_gdpy = random.choice(PYBOT_ANSWER_LOST)

    return first_answer_gdpy

def create_second_answer(result_description):
    """ Get second answer of GrandPy depending on the results of the MediaWiki API
    request returned """
    if result_description[2] and result_description[1] != '':
        second_answer_gdpy = random.choice(PYBOT_ANSWER_GET_STORY)
    else:
        second_answer_gdpy = random.choice(PYBOT_ANSWER_NO_STORY)

    return second_answer_gdpy

def answer_dictionnary(question):
    """ Main function:
    Return a jsonisable dictionnary with the answer from GrandPy, the address, the coordinates,
     the wiki article and its url """
    query_clean = analyse_question(question)

    result_apis = data_apis(query_clean)
    result_maps = result_apis[0]
    result_description = result_apis[1]
    first_answer_gdpy = create_first_answer(result_maps)
    second_answer_gdpy = create_second_answer(result_description)

    info_answer = {
        'query': query_clean,
        'first_answer_gdpy': first_answer_gdpy,
        'second_answer_gdpy': second_answer_gdpy,
        'latitude': result_apis[0][0],
        'longitude': result_apis[0][1],
        'address': result_apis[0][2],
        'found_place': result_apis[0][3],
        'description_wiki': result_apis[1][1],
        'url_wiki': result_apis[2],
        'respons_status_gmaps': result_apis[0][4],
        'req_url': result_apis[0][5]

    }

    return info_answer
