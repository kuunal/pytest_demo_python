from demo_operations import demo_operations
import pytest

demo_object =""

def setup_module(module):
    global demo_object
    demo_object = demo_operations()


def test_add():
    assert demo_object.add(3,4) == 7

def test_add_string():
    assert demo_object.add("Hello ","World") == "Hello World"
