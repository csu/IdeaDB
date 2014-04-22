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
        return self.collection.find_one({"_id": ObjectId(search_id)})

    def add(self, idea_body):
        idea = {"body": idea_body, "added": datetime.datetime.utcnow()}
        return self.collection.insert(idea)

    def test():
        return 'the ideadb object is working.'