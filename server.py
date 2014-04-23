#!/usr/bin/env python
from flask import Flask, jsonify, request
from ideadb import IdeaDB
from bson.objectid import ObjectId
import datetime
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

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

@app.route('/test', methods=['GET'])
def test():
    return db.test()

@app.route('/api/v1/idea/<idea_hash>', methods=['GET'])
def getIdea(idea_hash):
    if idea_hash == 'all' or idea_hash is None:
    	print 'going to getAll()'
        return getAll()
    try:
    	print 'going the single retrieve route'
        return JSONEncoder(sort_keys=True, indent=4, separators=(',', ': ')).encode(db.searchById(idea_hash))
    except:
        return jsonify({'error':'Invalid request'})

def getAll():
    try:
    	all_items = []
    	for item in db.getAll():
    		all_items.append(item)
    	return JSONEncoder(sort_keys=True, indent=4, separators=(',', ': ')).encode(all_items)
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/api/v1/idea/add', methods=['POST'])
def addIdea():
    try:
        body = request.form['body']
        return db.insert(body)
    except:
        return jsonify({'error':'Invalid request'})

if __name__ == '__main__':
    app.run(debug=True)