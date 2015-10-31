# encoding=utf-8_general_ci

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(r"./controllers")

from main import IndexHandler
from entry import EntryHandler
from getpic import getpicHandler

define("port", default=8081, help="run on the given port", type=int)

application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/s-getEntry", EntryHandler),
        (r"/s-getPic", getpicHandler),
        ],
        cookie_secret="61oETzKXQASENTENCEFuYh7EQnp2XdTP1o/Vo=",
        debug=True)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = application
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
