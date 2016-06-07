
from app.Dao.connection  import mongoDB

class analisysDao():


    conn = object

    def __init__(self):
        global conn
        self.conn = mongoDB()


    def getAllMeasure(self):
        collection = self.conn.analysis()
        return collection.find().limit(5)



    def saveMeasure(self, analytic):
         collection = self.conn.analysis()
         collection.insert(analytic.__dict__)

