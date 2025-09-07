import os

from flask import Flask
from flask import render_template, redirect, url_for, session, jsonify, send_from_directory, send_file, session

from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Define the path for the app
app.config['APP_PATH'] = os.path.dirname(os.path.abspath(__file__))
print(app.config['APP_PATH'])

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'


@app.route('/')
def home():
    return render_template('index.html')

''' API
'''

@app.route('/api/add-new-part')
def api_add_new_part():
    return 0

''' Views
'''

@app.route('/view/add-new-part')
def view_add_new_part():
    return render_template('add-new-part.html')