from flask import Flask, render_template, jsonify
from heavy import * 

# Import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


@app.route("/")
def welcome():

	return render_template('index.html', message="Welcome to Heavy API")

@app.route("/create/<file>")
def file_create(file):
	heavy = Heavy(file_name=file)
	return render_template('file.html', message=heavy.create_file())

@app.route("/compress/<file>")
def file_compress(file):
	heavy = Heavy(file_name=file)
	return render_template('file.html', message=heavy.compress_file())

@app.route("/show/operations")
def show_operations():
	return 69

if __name__ == '__main__':
    app.run(debug=True)