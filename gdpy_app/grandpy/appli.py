import json

from gdpy_app.grandpy.apiclients.googlemaps import Maps
from gdpy_app.grandpy.apiclients.wikipedia import Wiki
from gdpy_app.grandpy.parsers import QueryParser


userInput = "Hello GrandPy ! Tu connais l'adresse de l'aquarium Océanopolis à Brest ? "


def answer(question):
    """ Analyse the user's question, call the APIs and return a json dictionnary """ 
    ### Analyse the user's question
    query = QueryParser(userInput)
    # print(query.userInput)
    queryNormalize = query.normalize_query()
    # print(query.query_no_accent)
    queryClean = query.parser_words()
    print(query.query_words)

    ### Call the GoogleMaps API to get an address and coordinates 
    ## from the queryClean
    query_maps = Maps(query.query_words)
    query_maps.call_maps()
    # print(query_maps.latitude, query_maps.longitude, query_maps.formatted_address)

    ### Call the MediaWiki API to get the first lines from an article 
    ## corresponding to the queryClean
    query_wiki = Wiki(query.query_words)
    query_wiki.get_description_page_wiki()
    query_wiki.get_url_page_wiki()

    ### Return a jsonisable dictionnary with the answer from gdpy, the address, the coordinates, 
    ## the wiki article and its url
    info_answer = {
        'answer_gdpy': 'blabla',
        'query': queryClean,
        'latitude': query_maps.latitude,
        'longitude': query_maps.longitude,
        'address': query_maps.formatted_address,
        'description_wiki': query_wiki.description,
        'url_wiki': query_wiki.url
    }

    info_answer_json = json.dumps(info_answer)
    print(info_answer_json)

    return info_answer_json


# ans = answer(userInput)

