from app.calculator import calc

def test_addition():
    assert calc(2, 3, "add") == 5

def test_subtraction():
    assert calc(5, 2, "sub") == 3