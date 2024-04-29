from src.breeze.jijnja_util import get_jinja_env


def test_get_env():
    env = get_jinja_env()
    assert env
    print(env)

