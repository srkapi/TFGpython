from datetime import datetime


class file(object):

    def __init__(self, _name):
        self.name = _name
        self.date = datetime.now()