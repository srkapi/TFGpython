from datetime import datetime



class event(object):


    def __init__(self, _des, id):
        self.idEvent = id
        self.dateEvent= datetime.now()
        self.description = _des