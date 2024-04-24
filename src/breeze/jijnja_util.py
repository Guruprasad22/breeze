from jinja2 import Environment, FileSystemLoader


def get_jinja_env():
    env = Environment(loader=FileSystemLoader("templates/"))
    return env

