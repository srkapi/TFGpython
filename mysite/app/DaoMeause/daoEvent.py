
from connection import mongoDB

class daoEvent():

    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()


    def getAllEvent(self):
        collection = self.conn.event()
        return collection.find().limit(5)

    def getEvent(self, id):
        collection = self.conn.event()
        return collection.find({"idEvent": id}).limit(5)





    def saveEvent(self, event):
         collection = self.conn.event()
         collection.insert(event.__dict__)


