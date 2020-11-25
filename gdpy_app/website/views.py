"""
Module views.py:
- Create the routes for the application
- Send back the response to the AJAX query
"""
from flask import render_template, request, jsonify

from gdpy_app.website import app
from gdpy_app.grandpy import appli

# Config options - Make sure you created a 'config.py' file
# To get one variable, tape app.config['MY_VARIABLE']
app.config.from_object('config')

# Home page, so just '/'
@app.route('/')
def index():
    """ Function index that will be executed on the page "/" """
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """ Function process: create response to the AJAX query """
    #Get the question from the HTTP request
    req = request.form
    user_query = req.get('userInput')

    if user_query != '':
        # Get back a dictionnary
        result = appli.answer_dictionnary(user_query)

        # Transform the dictionnary in json HTTP respons and return this respons.
        if result:
            return jsonify({
                'userQuery': user_query,
                'cleanQuery': result['query'],
                'firstAnswerGdPy': result['first_answer_gdpy'],
                'secondAnswerGdPy': result['second_answer_gdpy'],
                'latitude': result['latitude'],
                'longitude': result['longitude'],
                'adress_formatted': result['address'],
                'found_place': result['found_place'],
                'url_wiki': result['url_wiki'],
                'description_wiki': result['description_wiki']
                })
        return jsonify({'error' : 'Missing data'})

    return jsonify({
            'userQuery': user_query,
            'cleanQuery': '',
            'firstAnswerGdPy': 'Faudrait peut-être écrire quelque chose...',
            # 'secondAnswerGdPy': '',
            # 'latitude': 'NULL',
            # 'longitude':  'NULL',
            'adress_formatted': '',
            'found_place': False,
            # 'url_wiki': '',
            # 'description_wiki': ''
            })
