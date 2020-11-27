****************************************************************************************************************
# P7_GrandPy-Bot
*Create a web interface where you can ask your way to Mr GrandPy Bot. This nice old man will answer you with a little story about the place and give you the location with a map from google maps !*
*****************************************************************************************************************

### About The Project:
Nostalgic of the discussions you had with your grandpa, the application GrandPy Bot is made for you! Don't forget...the interaction between the user and GrandPy is in french.

#### So how does it work?
##### Client part *visible from a web browser*:
*Is in charge of the dialog view:
Send user queries and receive the information for the answers of GrandPy.*
From the web interface: 
- The user enter is query and press enter button. The query is displayed on the dialog area.
- The sleeping face of GrandPy turns into a thinking face.
- The answers of GrandPy are then displayed below the user query in the dialog area.

##### Server part:
*Is in charge of the identification of the searched place, the localisation and the place descripiton:
Process the query sending from the user (client part) and research the different informations of the answer of GrandPy.*
- Analyse the user query
- Request GoogleMaps API to find an address and the coordinates to display a map.
- Request MediaWiki API to get few lines from a wiki page concerning a part of the user query.
- Create the answer of GrandPy depending of the request results.

#### Built With:
##### Languages and tools used:
	* Python 3.8.2 and its framework Flask
	* HTML5, CSS3, JS
	* Responsiv design with Bootstrap
	* Dynamic update of the application view with AJAX function
	* Test driven development
##### API:
	* GoogleMaps: in order to get an address from the user input and display a map.
	* MediaWiki: in order to have information about the user input so that GrandPy can tell a little story.

### Architecture:
.env
config.py
requirements.txt
run.py
gdpy_app
	grandpy
		appli.py
		parsers.py
		words.py
		apiclients
			googlemaps.py
			wikipedia.py
		tests
			test_parsers.py
			test_appli.py
			apiclients
				test_googlemaps.py
				test_wikipedia.py
				dataSet_mocks.json
	website
		static
			css
			fonts
			img
			js
		templates
			index.html
		views.py

### Getting Started:
##### Prerequisites:
Python must be installed.
Virtualenv Module too, otherwise : 
	* pip install virtualenv

##### Installation:
###### Local version:
	1- Clone this repository: git clone https://github.com/MarionGiusti/P7_GrandPy-Bot

	2- Create a virtualenv in P7_GrandPy-Bot: virtualenv -p python3 env

	3- Activate the virtualenv:
		Linux & MacOS user: source pb_env\bin\activate
		Windows user: pb_env\Scripts\activate

	4- Install the required libraries list in the requirements.txt file: pip install -r requirements.txt

	6- Create a .env file in root of the repository. Write in it your GoogleMaps API Key:
	GOOGLEMAPS_KEY=yourkey

	7- Run the program on your terminal:
	run.py

By default, after running the application will be accessible here: http://127.0.0.1:5000/

###### Online version:
The application is deployed on Heroku:  
https://grandpybot-is-your-guide.herokuapp.com/

### Features:
The program counts 3 classes: QueryParser, Maps and Wiki.
#### Classes:
##### QueryParser Class: parsers.py
Methods to clean the user input
	* normalize_query(): lower the letter, remove accent and punctuations.
	* parser_words(): remove stop words in order to have a kind of filter to keep the most indicative part.
Get a clean query !

##### Maps Class: googlemaps.py
Method to request the GoogleMaps API
	* call_maps() : call the api with the clean query. From the json response, get coordinates and address. If 'status error' in the json respon, assign coordinates and address corresponding to a place for GrandPy holidays.

##### Wiki Class: wikipedia.py
Method to request the MediaWiki API
	* wiki_api_call(): call the api with the clean query and get json respons.

Methods to define the parameters of the request
	* get_description_page_wiki(): parameters to get a description of a wiki page.
	* get_url_page_wiki(): parameters to get the url of the wiki page used for the description.

#### Main function: appli.py
Functions to create instances from the QueryParser, Maps and Wiki classes.
	* analyse_question(), data_apis()
Functions to create GrandPy's answers depending on the api responses.
	* create_first_answer(), create_second_answer()
Function to create a dictionnary with all the informations useful to send back to the client part.
	* answer_dictionnary()

### Usage:
The user enter in the input form a question about a place he would like to localise:
	"Hello GrandPy! Est-ce-que tu connais l'adresse de l'aquarium Océanopolis à Brest?"

The user input will be display above in the dialog area.
It wakes up GrandPy, its picture change, he is thinking...

###### GrandPy found a place:
A first answer will appear and a map with the localication of the address. He can reply something like this:
 "Mais oui mon biquet ! Là voilà :" + the address
Then if GrandPy found a story about the user input, he may say:
	"Dis poussin, je t'ai déjà raconté cette histoire?" + few lines about the story
But if no memory comes to him, he will probably say:
	"Fichtre! Je me souviens plus ce que je voulais te raconter..."

##### GrandPy didn't found a place:
Only one answer will appear. GrandPy will reply with a random answer and say that he needs holidays:
	"Ca aurait été avec plaisir mon poussin, mais là je ne me souviens plus...\n
	demande moi autre chose!" + "J'ai besoin de vacances...Regarde la carte, tu connais ce coin?"
