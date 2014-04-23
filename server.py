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

@app.route('/test', methods=['GET'])
def test():
    return db.test()

@app.route('/api/v1/idea/<idea_hash>', methods=['GET'])
def getIdea(idea_hash):
    try:
        return db.searchById(idea_hash)
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