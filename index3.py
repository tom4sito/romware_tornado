# import jinja2
from jinja2 import Environment, FileSystemLoader

# import os module
import os.path

# import tornado
import tornado.ioloop
import tornado.web
import tornado.httpserver

# developer mode on
settings = {
	'debug':True,
	"static_path": os.path.join(os.path.dirname(__file__), "static")
	# other stuff
}


# Load template file templates/site.html
TEMPLATE_FILE="site.html"
templateLoader = FileSystemLoader(searchpath="templates")
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template(TEMPLATE_FILE)

# list of items
items = ["Item 1", "item 2", "item 3"]

# template.render() returns a string containing the rendered HTML
html_output = template.render(items=items)

#Handler for main page
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#Returns rendered template string to the browser request
		self.write(html_output)

#Assign handler to the server root
def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	], **settings)

if __name__ == "__main__":
	app = make_app()
	server = tornado.httpserver.HTTPServer(app)
	server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

# if __name__ == "__main__":
# 	server = tornado.httpserver.HTTPserver()
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()