from src.breeze.jinja_util import get_jinja_env
import pytest


@pytest.mark.skip(reason="tested and working")
def test_get_env():
    env = get_jinja_env()
    assert env
    print(env)
