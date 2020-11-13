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
# """ 
# 1. Récupérer la question depuis la requête HTTP
# 2. appeler la fonction answer, en lui envoyant la question du visiteur en argument, et en récupérant le dictionnaire retourné
# 3. Transforme le dictionnaire retourné en réponse HTTP json et retourne cette réponse.
# """
def process():
	# result = request.form['userInput'];
	req = request.form
	result1 = req.get('userInput')

	result = appli.answer(result1)
	



	if result:
		return jsonify({'result': 'user: ' + result[0]})
	return jsonify({'error' : 'Missing data'})