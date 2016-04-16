
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

    def findUserByUserName(self, name):
        collection = self.conn.user()
        user = collection.find({'user': name})
        return user


    def updateUser(self,user):
        collection = self.conn.user()
        collection.find_and_modify(query={'user': user.user}, update={"$set": {
                                    'password': user.password,
                                    'name': user.name,
                                    'lastName': user.lastName,
                                    'email': user.email}},
                                    upsert=False, full_response= True)



    def deleteUser(self,user):
        collection = self.conn.user()
        collection.find_and_modify(query={'user': user.user}, update={"$set": {
                                    'activo': 0}},
                                    upsert=False, full_response= True)


