#! /usr/bin/env python

"""
GrandPy Bot application: Ask and he will guide you !
This application gives you an address, a maps and a little
story of the location that you asked.

Flask Application and Python scripts
Files:
run.py (main script),
	* gdpy_app (the Flask app)
		* Package website:
			views.py (give the routes)
			scripts html, js and css
		* Package grandpy:
			appli.py, parsers.py, words.py (modules)
			* Package apiclients
			googlemaps.py and wikipedia.py (modules)
"""

from gdpy_app.website import app

if __name__ == "__main__":
    app.run(debug=True)
    