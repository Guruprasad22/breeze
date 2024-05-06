from jinja2 import Environment, FileSystemLoader
import pytest


@pytest.mark.skip(reason="tested and working")
def get_jinja_env():
    env = Environment(loader=FileSystemLoader("templates/"))
    return env


@pytest.mark.skip(reason="tested and working")
def get_template(env, template_name):
    return env.get_template(template_name)
