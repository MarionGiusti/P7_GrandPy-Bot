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

def answer(question):
    """ Analyse the user's question, call the APIs and return a json dictionnary """
    ### Analyse the user's question
    query = QueryParser(question)
    query.normalize_query()
    query_clean = query.parser_words()

    ### Call the GoogleMaps API to get an address and coordinates
    ## from the queryClean
    query_maps = Maps(query.query_words)
    query_maps.call_maps()
    # print(query_maps.latitude, query_maps.longitude, query_maps.formatted_address)
    if query_maps.formatted_address == '':
        first_answer_gdpy = random.choice(PYBOT_ANSWER_LOST)
        query_maps.formatted_address = \
        "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"
    else:
        first_answer_gdpy = random.choice(PYBOT_ANSWER_GOOD)


    ### Call the MediaWiki API to get the first lines from an article
    ## corresponding to the queryClean
    query_wiki = Wiki(query.query_words)
    query_wiki.get_description_page_wiki()
    query_wiki.get_url_page_wiki()

    if query_wiki.description == '':
        second_answer_gdpy = random.choice(PYBOT_ANSWER_NO_STORY)
        query_wiki.description = ''
        query_wiki.url = 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'
    else:
        second_answer_gdpy = random.choice(PYBOT_ANSWER_GET_STORY)


    ### Return a jsonisable dictionnary with the answer from gdpy, the address, the coordinates,
    ## the wiki article and its url
    info_answer = {
        'query': query_clean,
        'first_answer_gdpy': first_answer_gdpy,
        'second_answer_gdpy': second_answer_gdpy,
        'latitude': query_maps.latitude,
        'longitude': query_maps.longitude,
        'address': query_maps.formatted_address,
        'found_place': query_maps.found_place,
        'description_wiki': query_wiki.description,
        'url_wiki': query_wiki.url
    }

    return info_answer
