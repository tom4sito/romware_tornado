import tornado.ioloop
import tornado.web
import jinja2

class JinjaRenderer(tornado.web.RequestHandler):
    def render_template(self, template_name, **kwargs):
        template_dirs = []
        if self.settings.get('', ''):
            template_dirs.append(
            self.settings['']
        )
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dirs))
        try:
            template = env.get_template(template_name)
        except jinja2.TemplateNotFound:
            raise jinja2.TemplateNotFound(template_name)
        return template.render(kwargs)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	items = ["Item 1", "item 2", "item 3"]
    	self.render("template.html", title="SR60", items=items)

def make_app():
    return tornado.web.Application([
        (r"/", JinjaRenderer),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()