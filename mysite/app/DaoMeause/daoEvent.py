
from connection import mongoDB

class daoEvent():

    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()


    def getAllEvent(self):
        collection = self.conn.event()
        return collection.find()

    def getEvent(self,):
        collection = self.conn.event()
        return collection.find()





    def saveEvent(self, event):
         collection = self.conn.event()
         collection.insert(event.__dict__)


