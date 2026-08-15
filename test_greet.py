from greet import greet


def test_greet_basic():
    assert greet("world") == "Hello, world!"
