from demo_operations import demo_operations
import pytest

demo_object =""

def setup_module(module):
    global demo_object
    demo_object = demo_operations()

@pytest.mark.numbers
def test_add():
    assert demo_object.add(3,4) == 7

@pytest.mark.string
def test_add_string():
    assert demo_object.add("Hello ","World") == "Hello World"

@pytest.mark.numbers
def test_product():
    assert demo_object.product(2,5) == 10

@pytest.mark.string
def test_product_string():
    assert demo_object.product("Hello",3) == "HelloHelloHello" 