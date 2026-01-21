from flask import Flask, send_from_directory
import os

dist_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'dist')
app = Flask(__name__, static_folder=dist_path, static_url_path='')

# Serve HTML
@app.route('/', defaults={'path': ''})
@app.route("/<string:path>")
def index(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)