from utils import suma


def test_suma():
    assert suma(2, 4) == 6
    assert suma(5, 7) == 12
    assert suma(10, 5) == 15
    assert suma(20, 15) == 35
    assert suma(20, 40) == 60
    assert suma(20, 20) == 40
    assert suma(30, 30) == 60 
