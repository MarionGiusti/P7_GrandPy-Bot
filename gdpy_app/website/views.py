from flask import render_template, url_for, request, jsonify


from gdpy_app.website import app
from gdpy_app.grandpy import appli

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

## Define a page with Flask. @gdpy_app precise at which adress, what's follow will apply
# Home page, so just '/'
@app.route('/')
# Function index that will be executed on the page "/"
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
# Function index for the Ajax query
def process():
	# Get the question from the HTTP request
	# result = request.form['userInput'];
	req = request.form
	userQuery = req.get('userInput')

	# Call the function answer with the user input in argument. Get back a dictionnary
	result = appli.answer(userQuery)
	
	firstAnswerGdPy = result['first_answer_gdpy']
	secondAnswerGdPy = result['second_answer_gdpy']
	cleanQuery = result['query']
	latitude = result['latitude']
	longitude = result['longitude']
	adress_formatted = result['address']
	found_place = result['found_place']
	url_wiki = result['url_wiki']
	description_wiki = result['description_wiki']

	# Transform the dictionnary in json HTTP respons and return this respons.
	if result:
		return jsonify({
			'userQuery': userQuery,
			'cleanQuery': cleanQuery, 
			'firstAnswerGdPy': firstAnswerGdPy,
			'secondAnswerGdPy': secondAnswerGdPy,
			'latitude': latitude,
			'longitude': longitude,
			'adress_formatted': adress_formatted,
			'found_place': found_place,
			'url_wiki': url_wiki,
			'description_wiki': description_wiki
			})
	return jsonify({'error' : 'Missing data'})