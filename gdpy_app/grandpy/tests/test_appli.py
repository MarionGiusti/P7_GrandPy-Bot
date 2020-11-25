"""
Test the module apply.py
"""
from gdpy_app.grandpy import appli

QUESTION = "Hello GrandPy! Tu sais où se trouve l'aquarium Océanopolis à Brest?"

def test_get_query_clean():
    assert appli.analyse_question(QUESTION) == "aquarium oceanopolis brest"

def test_get_first_answer_gdpy_if_found_place_false():
    result_maps = (0,0,'', False)
    first_answer_gdpy = appli.create_first_answer(result_maps)
    assert first_answer_gdpy in appli.PYBOT_ANSWER_LOST

def test_get_first_answer_gdpy_if_found_place_true():
    result_maps = (48.3899736, -4.4356012,
         'Port de Plaisance du Moulin Blanc, 29200 Brest, France', True)
    first_answer_gdpy = appli.create_first_answer(result_maps)
    assert first_answer_gdpy in appli.PYBOT_ANSWER_GOOD

def test_get_second_answer_gdpy_if_no_description():
    result_description = (['0'], '', False)
    second_answer_gdpy = appli.create_second_answer(result_description)
    assert second_answer_gdpy in appli.PYBOT_ANSWER_NO_STORY

def test_get_second_answer_gdpy_if_description():
    result_description = (['150231'],
        'Océanopolis est un centre de culture scientifique consacré aux océans, '\
         'situé à Brest, près du port de plaisance du Moulin Blanc.', True)
    second_answer_gdpy = appli.create_second_answer(result_description)
    assert second_answer_gdpy in appli.PYBOT_ANSWER_GET_STORY
