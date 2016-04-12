
import json


class user(object):

    def __init__(self , name_, lastname_, email_, pass_,user_):
        self.name= name_
        self.lastName= lastname_
        self.user= user_
        self.password= pass_
        self.email= email_



    def dataJSON(self):
        return json.dump(self)