import tornado.ioloop
import tornado.web
import os
current_path = os.path.dirname(os.path.abspath(__file__))
settings = {
    'template_path': current_path,
    'static_path': current_path + '/static'
}
class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("cloud-index.html")
def make_app():
    routelist = [
        (r"/",Index),
    ]
    return tornado.web.Application(routelist, **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(2333)
    tornado.ioloop.IOLoop.current().start()
