import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

# Define the path for the app
app.config['APP_PATH'] = os.path.dirname(os.path.abspath(__file__))

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'

#Import routes
from . import routes

''' --- API ---
'''

''' Part
'''


''' --- VIEWS ---
'''

