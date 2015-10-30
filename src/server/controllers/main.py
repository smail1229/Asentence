
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("user", "adm")
        self.write("hello world!\n")