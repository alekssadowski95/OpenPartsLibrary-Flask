from openpartslibrary_flask import app

if __name__ == '__main__':
    print("Starting OpenPartsLibrary Server")
    app.run(host="localhost", port=5000, debug=True)
    