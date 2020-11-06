from flask import Flask, render_template, url_for

# Give the name of the application, here app
app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

## Define a page with Flask. @gdpy_app precise at which adress, what's follow will apply
# Home page, so just '/'
@app.route("/")
@app.route("/index/")
# Function index that will be executed on the page "/"
def index():
	return render_template("index.html")