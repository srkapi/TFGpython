

from pymongo import MongoClient

class mongoDB(object):

    conn = object

    def __init__(self):
        global conn
        self.conn = MongoClient()
        self.db = conn.connec['project']


    def user(self):
        return self.db.app_user


    def measure(self):
        return self.measure


