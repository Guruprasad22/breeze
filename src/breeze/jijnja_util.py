from jinja2 import Environment, FileSystemLoader


def get_jinja_env():
    env = Environment(loader=FileSystemLoader("templates/"))
    return env


def get_template(env, template_name):
    return env.get_template(template_name)

