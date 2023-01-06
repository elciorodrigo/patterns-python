import os
import tornado.ioloop
import tornado.web


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listem(5000)
    tornado.ioloop.IOLoop.instance().start()