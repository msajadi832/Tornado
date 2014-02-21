import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pycket.session import SessionManager
from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # session = SessionManager(self)
        # if session.get("LoggedIn","No") != "No" :
        #     session.set('info', {"Ln":"Alavi","Fn":"ali"})
        #     session.set('_id','1233444')
            self.render('index.html',UN="Welcome Back .U Are Logged In")
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")





class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        session = SessionManager(self)
        # if session.get()
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        us = self.get_current_user()
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,difference=noun3,user = us,ID=session.get('_id'),INFO=session.get('info'))




if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],debug=True,
        cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path= os.path.join(os.path.dirname(__file__), "static"),
        **{
        'pycket': {
            'engine': 'redis',
            'storage': {
                'host': 'localhost',
                'port': 6379,
                'db_sessions': 10,
                'db_notifications': 11,
                'max_connections': 2 ** 31,
                },
            'cookies': {
                'expires_days': 120,
                },
            },
            }

        )


    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()