
from base import base
import os.path
from config import *

class getpicHandler(base):
    def get(self):
        if self.initial() == False:
            self.write("Error!")
            return

        pic_type = self.get_argument("type", "")
        pic_name = self.get_argument("name", "")

        if pic_type not in ["avatar", "pics"]:
            self.write("argument error!")
            return

        if pic_type == "avatar":
            file_path = os.path.join(upload_path, "avatar", str(pic_name))
        elif pic_type == "pics":
            file_path = os.path.join(upload_path, "pics", str(pic_name))

        self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename= %s' % (pic_type + str(pic_id) + ".png"))

        with open(file_path, 'rb') as f:
            while True:
                data = f.read(8000)
                if not data:
                    break
                self.write(data)

        self.finish()