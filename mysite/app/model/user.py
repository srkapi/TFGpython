
import json


class user(object):

    def __init__(self , name_, lastname_, email_, pass_, user_, _admin, _activo):
        self.name= name_
        self.lastName= lastname_
        self.user= user_
        self.password= pass_
        self.email = email_
        self.activo = 1
        self.admin = _admin
        self.activo = _activo




    def dataJSON(self):
        return json.dump(self)