from pymongo import MongoClient
from bson.objectid import ObjectId
import secret
import datetime
import hashlib

class IdeaDB(object):
    def __init__(self):
        self.client = MongoClient('mongodb://' + secret.MONGO_DB_USER + ':' + secret.MONGO_DB_PASS + '@ds029287.mongolab.com:29287/ideadb')
        self.database = self.client.ideadb
        self.collection = self.database.ideas

    def searchById(self, idea_hash):
        return self.collection.find_one({"hash": idea_hash})

    def insert(self, idea_body):
        idea = dict()
        idea['body'] = idea_body
        idea['added'] = datetime.datetime.utcnow()
        idea['hash'] = hashlib.sha224(str(idea)).hexdigest()
        self.collection.insert(idea)
        return idea['hash']

    def test(self):
        return 'the ideadb object is working.'