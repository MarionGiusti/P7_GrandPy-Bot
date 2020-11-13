from flask import Flask

# Give the name of the application, here app
app = Flask(__name__)


from gdpy_app.website import views