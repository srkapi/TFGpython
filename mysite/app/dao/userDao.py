
import connection
from datetime import datetime
from models import Post,Measure , Users
import json


class daoUser(object):

    def __init__(self):
        self.connection = connection()

    def userMeasure(self , measure):
        collection = connection.user();
        value = json.dumps(measure, default=lambda x:x.__dict__)
        collection.insert(value)

