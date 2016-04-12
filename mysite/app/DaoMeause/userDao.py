
from connection import mongoDB
import json


class daoUser():

    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()

    def addUser(self, user):
        collection = self.conn.user()
        #value = json.dumps(user, default=lambda x:x.__dict__)
        collection.insert(user.__dict__)


    def getAll(self):
        collection = self.conn.user()
        return collection.find()


