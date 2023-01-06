import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver

from urls import IndexHandler, NewHandler, UpdateHandler, DeleteHandler

class RunApp(tornado.web.Application):
    
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'todo/update/(\d+)/status/(\d+)', UpdateHandler)
            (r'todo/delete/(\d+)', DeleteHandler),
        ]

        settings = dict(
            debug=True,
            template_path='templates',
            static_path="static",
        )

        tornado.web.Application.__init__(self, Handlers, **settings)