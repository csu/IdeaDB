from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import secret
import datetime

class IdeaDB(object):
    def __init__(self):
        client = MongoClient('mongodb://' + secret.MONGO_DB_USER + ':' + secret.MONGO_DB_PASS + '@ds029287.mongolab.com:29287/ideadb')
        database = client.ideadb
        collection = database.ideas

    def searchById(self, search_id):
        print 'in searchById with: ' + search_id
        return collection.find_one({"_id": ObjectId(str(search_id))})

    def insert(self, idea_body):
        idea = dict()
        idea['body'] = idea_body
        idea['added'] = datetime.datetime.utcnow()
        return self.collection.insert(idea)

    def test(self):
        return 'the ideadb object is working.'