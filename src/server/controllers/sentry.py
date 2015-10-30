
import tornado.web
from base import base

from bson.objectid import ObjectId

class EntryHandler(base):
    def get(self):
        if self.initial() == False:
            self.write("Error")
            return

        try:
            start = int(self.get_argument("start", ""))
            limit = int(self.get_argument("limit", ""))
        except:
            self.write("Error!")
            return

        result = self.db.entry.find().skip(int(start)).limit(int(limit))

        for each in result:
            each["_id"] = str(each["_id"])
            self.write(each)

