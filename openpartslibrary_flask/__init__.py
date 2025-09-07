import os

from flask import Flask
from flask import render_template


app = Flask(__name__)

# Define the path for the app
app.config['APP_PATH'] = os.path.dirname(os.path.abspath(__file__))

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'


''' --- API ---
'''

''' Part
'''
@app.route('/api/create-part')
def api_create_part():
    return 0

@app.route('/api/read-part')
def api_read_part():
    return 0

@app.route('/api/update-part')
def api_update_part():
    return 0

@app.route('/api/delete-part')
def api_delete_part():
    return 0

@app.route('/api/read-all-parts')
def api_read_all_parts():
    return 0


