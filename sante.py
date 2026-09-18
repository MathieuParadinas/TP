def sante(taille, poids):
    """Permet de détecter un pb de santé en foncton de l'imc

    Args:
        taille (float): La taille de la personne
        poids (int): Le poids de la personne

    Returns:
        str: Le problème de santé détecté
    """
    imc = poids / (taille * taille)
    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"
    elif imc < 25:
        res = "normal"
    elif imc < 30:
        res = "surpoids"
    else:
        res = "obésité"

    return res

def test_sante():
    assert sante(1.8, 80) =="normal" #indique que sante(1.8, 80) doit retourner "normal"
    assert sante(1.6, 67) =="surpoids" #indique que sante(1.6, 67) doit retourner "surpoids"
    assert sante(1.7, 90) =="obésité" #indique que sante(1.7, 90) doit retourner "obésité"
    assert sante(1.5, 40) =="maigreur" #indique que sante(1.5, 40) doit retourner "maigreur"
    assert sante(1.8, 50) =="famine" #indique que sante(1.8, 50) doit retourner "famine"
    assert sante(1.75, 65) == "normal"

print(sante(1.75, 70))
laTaille = float(input("Entrez votre taille en mètre : "))
lePoids = int(input("Entrez votre poids en kg : "))
print(sante(laTaille, lePoids))
