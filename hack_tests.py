from hack_power import hack_calculator


def test_baaca():
    assert hack_calculator('baaca') == 31


def test_babacaba():
    assert hack_calculator('babacaba') == 55


def test_aabacabaaaca():
    assert hack_calculator('aabacabaaaca') == 81


def test_abc():
    assert hack_calculator('abc') == 6


def test_baad():
    assert hack_calculator('baad') == 0
