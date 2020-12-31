from helloworld2 import say_hello

def test_helloworld2_no_params():
    assert say_hello() == "Hello, World!"

def test_helloworld2_with_params():
    assert say_hello("Anup") == "Hello, Anup!"