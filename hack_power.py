import re
from collections import OrderedDict


PHRASES_POWER = OrderedDict([('baa', 20), ('ba', 10)])
LETTERS_POWER = {'a': 1, 'b': 2, 'c': 3}


def _power_from_letters(hack):
    letters_instances = {letter: 0 for letter in LETTERS_POWER}
    power = 0
    for letter in hack:
        if letter not in LETTERS_POWER:
            return 0
        else:
            letters_instances[letter] += 1
            power += letters_instances[letter] * LETTERS_POWER[letter]
    return power


def _power_from_phrases(hack):
    power = 0
    for phrase in PHRASES_POWER:
        power += sum(PHRASES_POWER[phrase] for _ in re.finditer(phrase, hack))
        hack = re.sub(phrase, '', hack)
    return power


def hack_calculator(hack):
    """
    Calculate power of a given hack
    :param str hack: hack to calculate power
    :return: int power: power of hack
    """
    power_from_letters = _power_from_letters(hack)
    return 0 if power_from_letters == 0 else power_from_letters + _power_from_phrases(hack)
