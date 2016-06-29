from app.Dao.connection import mongoDB


class MeasureDao:
    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()

    def saveData(self, measure):
        connection = self.conn.measure()
        connection.insert(measure.__dict__)
