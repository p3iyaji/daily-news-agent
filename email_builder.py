from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('digest.html')

def build_email(articles):
    return template.render(articles=articles)
