import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "select * from task"
        todos = _execute(query)
        self.render('index.html', todos=todos)

class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task(id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)"
        _execute(query)
        query = "insert into task (name, status) values (%s, %d)" %(name, 1)
        _execute(query)
        self.redirect('/')

class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = "update task set status =%d where id=%s" %(int(status), id)
        _execute(query)
        self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = "delete from task where id=%s" % id
        _execute(query)
        self.redirect('/')