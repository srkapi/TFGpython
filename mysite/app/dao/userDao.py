
import connection
from datetime import datetime
from models import Post,Measure , Users
import json


class daoUser(object):

    def __init__(self):
        self.connection = connection()

    def userMeasure(self , user):
        collection = connection.user();
        value = json.dumps(user, default=lambda x:x.__dict__)
        collection.insert(value)


    def updateUser(self,user):
         collection = connection.user();
         value = json.dumps(user, default=lambda x:x.__dict__)



