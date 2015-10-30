import pymongo
from pymongo import MongoClient

import tornado.web

class base(tornado.web.RequestHandler):
    user = None
    db = None
    response = {
        "status" : 0,
        "message" : "",
        "data" : None
    }
    def initial(self):
        #if not self.get_secure_cookie('user'):
        #    return False

        #username = self.get_secure_cookie("user")

        client = MongoClient('localhost', 27017)
        self.db = client['Asentence']

        #users = self.db.user

        #self.user = users.find({"username" : username})

        #if self.user["authenticated"] == 1:
        #    return True

        return True
