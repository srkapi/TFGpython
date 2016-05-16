
from connection import mongoDB

class fileDao():

    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()



    def saveFile(self , file):
        connection = self.conn.file()
        connection.insert(file.__dict__)


    def getAll(self):
        connection = self.conn.file()
        return connection.find()


