def algo1(a,b,c,d):
    """Cherche le nombre le plus petit dans la liste des 4 chiffres

    Args:
        a (int): 1er chiffre
        b (int): 2ième chiffre
        c (int): 3ième chiffre
        d (int): 4ième chiffre

    Returns:
        int: le plus petit des 4 chiffres
    """
    res = 0
    if a < b:
        res = a
    else:
        res = b
    if c < res:
         res = c
    if d < res:
        res = d
    return res


def test_algo1():
    assert algo1(8, 10, 2, 15) == 2
    assert algo1(5, 3, 7, 1) == 1
    assert algo1(12, 9, 14, 11) == 9
    assert algo1(4, 4, 4, 4) == 4
    assert algo1(-5, -3, -7, -1) == -7
    assert algo1(8, 10, 2, 15) == 2

def algo2(mot):
    """On cherche le nombre de voyelles dans note mot"""
    res = 0
    for lettre in mot:
        if lettre in "aeiouy":
            res = res + 1
    return res


def test_algo2():
    assert algo2("bonjour") == 3
    assert algo2("python") == 2
    assert algo2("ordinateur") == 5
    assert algo2("programmation") == 5
    assert algo2("exercice") == 4
