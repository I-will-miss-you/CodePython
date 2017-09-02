def maximo(x, y):
    return x if x > y else y


def test_answer():
    assert maximo(6, 5) == 6
    assert maximo(-6, 5) == 5
    assert maximo(6, 6) == 6
    assert maximo(6, -5) == 6
