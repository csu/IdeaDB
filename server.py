#!/usr/bin/env python

from flask import Flask, jsonify, request
from ideadb import IdeaDB

app = Flask(__name__)

db = IdeaDB()

@app.route('/', methods=['GET'])
def index():
	programInfo = dict()
	programInfo['author'] = 'Christopher Su'
	programInfo['author_url'] = 'http://christophersu.net/'
	programInfo['name'] = 'IdeaDB'
	programInfo['version'] = '1.0.0'
	programInfo['project_url'] = 'http://github.com/csu'
	programInfo['source_url'] = 'http://github.com/csu/IdeaDB/'
	programInfo['description'] = 'A database and API for saving and accessing ideas.'
	return jsonify(programInfo)

@app.route('/test/', methods=['GET'])
def test():
	return db.test()

if __name__ == "__main__":
    app.run()