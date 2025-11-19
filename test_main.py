from main import add, subtract, floating_number

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 7) == -2

def test_floating_number():
    assert floating_number(50) == 227.272727
