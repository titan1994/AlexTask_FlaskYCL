from flask import render_template, request
from app_flask import app

from app_flask.api_back.migration_metadata.metadata_processing import process_metadata


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/test', methods=['GET', 'POST'])
def test():
    return '["tool":41235]'


@app.route('/get_metadata', methods=['POST'])
def get_metadata():
    json_in = request.json
    json_out = process_metadata(json_in)
    return json_out

