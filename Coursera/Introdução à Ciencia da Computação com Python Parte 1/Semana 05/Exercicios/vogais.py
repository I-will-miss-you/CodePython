def vogal(letra):
    vogais = "aeiou"
    if letra.lower() in vogais:
        return True
    return False


def test_answer():
    assert vogal('a') == True
    assert vogal('z') == False
    assert vogal('A') == True
    assert vogal('Z') == False