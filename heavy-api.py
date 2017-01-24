# Notes:
# Author: Marcin Taracha
# Version: 1.0

from flask import Flask, render_template, jsonify, abort, request, make_response, url_for
from heavy import * 

# Import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/v1/api")
def welcome():

	return make_response(jsonify({'message': 'Welcome to Heavy API'}), 200) 

@app.route("/v1/api/create/<file>")
def file_create(file):
	
	heavy = Heavy(file_name=file)
	
	return make_response(jsonify({'message': heavy.create_file()}), 200) 

@app.route("/v1/api/compress/<file>")
def file_compress(file):
	
	heavy = Heavy(file_name=file)

	return make_response(jsonify({'message': heavy.compress_file()}), 200) 

@app.route("/v1/api/show/operations")
def show_operations():
	return 69

if __name__ == '__main__':
    app.run(debug=True)