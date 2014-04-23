from pymongo import MongoClient
from bson.objectid import ObjectId
import secret
import datetime
import hashlib
import os

class IdeaDB(object):
    def __init__(self):
        if 'MONGOLAB_URI' in os.environ:
            self.client = MongoClient(os.environ['MONGOLAB_URI'])
        else:
            self.client = MongoClient(secret.MONGO_DB_PATH)
        self.database = self.client.ideadb
        self.collection = self.database.ideas

    def searchById(self, idea_hash):
        return self.collection.find_one({"hash": idea_hash})

    def getAll(self):
        return self.collection.find()

    def insert(self, idea_body):
        idea = dict()
        idea['body'] = idea_body
        idea['added'] = datetime.datetime.utcnow()
        idea['hash'] = hashlib.sha224(str(idea)).hexdigest()
        self.collection.insert(idea)
        return idea['hash']
