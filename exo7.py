def algo1(genre, PR, nb_Coursesgagné, Champion):
    """On cherche à savoir si la personne, en fonction de son genre, de son PR et du nombre de course gagné, ou si elle est champion(nne) dans sa discipile, si elle peut se qualifié à la compétition"""
    if Champion == "oui":
        Champion = True
    else:
        Champion = False
    if genre == "h":
        if PR < 12 and nb_Coursesgagné >= 3:
            res = "qualifié"
        elif Champion == True:
            res = "qualifié"
        else:
            res = "non qualifié"
    elif genre == "f":
        if PR < 15 and nb_Coursesgagné >= 3:
            res = "qualifié"
        elif Champion == True:
            res = "qualifié"
        else:
            res = "non qualifié"
    else:
        res = "genre non reconnu"

    return res



def test_algo1():
    assert algo1("h", 11, 3, 5, "oui") == "qualifié"
    assert algo1("f", 14, 4, 6, "non") == "qualifié"
    assert algo1("h", 13, 2, 4, "oui") == "qualifié"
    assert algo1("f", 16, 1, 3, "oui") == "qualifié"
    assert algo1("h", 13, 2, 4, "non") == "non qualifié"
    assert algo1("f", 16, 1, 3, "non") == "non qualifié"
    assert algo1("x", 10, 5, 7, "oui") == "genre non reconnu"

genre = str(input("Entrez votre genre (h/f) : "))
PR = float(input("Entrez votre PR : "))
nb_Coursesgagné = int(input("Entrez le nombre de courses gagnées : "))
Champion = str(input("Êtes-vous champion(ne) dans votre discipline ? (oui/non) : "))
print(algo1(genre, PR, nb_Coursesgagné, Champion))