




from pymongo import  Connection

class mongoDB():
    conn = object

    def __init__(self):
        global conn
        self.conn = Connection("localhost", 27017)
        self.db = self.conn.connec['project']


    def user(self):
        db = self.conn['project']
        collection = db.app_user
        return collection


    def measure(self):
        db = self.conn['project']
        collection = db.app_measure
        return collection


    def event(self):
        db = self.conn['project']
        collection = db.app_event
        return collection


