from openpartslibrary_flask import app
from flask import Flask
from openpartslibrary_flask.routes import Routes

app = Flask(__name__)
Routes(app)

if __name__ == '__main__':
    print("Starting OpenPartsLibrary Flask Server")
    app.run(host="localhost", port=5000, debug=True)
    