def amende(vitesse, limite, recidive):
    """On veut calculer le montant de l'amende, le nombre de points perdus, le temps de supension du permis, et le nombre de temps de prison en fonction de la vitesse du conducteur lors du dépassement, de la limite de vitesse, du nombre de sanctions déjà reçues et du montant de base de l'amende.


    Args:
        vitesse (int): La vitesse de la voiture lors du dépassement
        limite (int): la limite de vitesse lors du dépassement
        recidive (bool): Indique si le conducteur est récidiviste

    Returns:
        Le montant de l'amende en euro, le nombre de points perdus, le temps de suspension du permis en année, et le temps de prison en année
    """
    if vitesse - limite == 20: #on  regarde si l'excès de vitesse est de 20 km/h
        if limite >= 50: #on regarde si la limite de vitesse est supérieure ou égale à 50 km/h
            montant = 68
            point = 1
            suspension = 0
            prison = 0
        else: #la limite de vitesse est inférieure à 50 km/h
            montant = 135
            point = 1
            suspension = 0
            prison = 0
    elif vitesse - limite >= 20 and vitesse - limite <= 30: #on regarde si l'excès de vitesse est compris entre 20 et 30 km/h
        montant = 135
        point = 2
        suspension = 0
        prison = 0
    elif vitesse - limite >= 30 and vitesse - limite <= 40: #on regarde si l'excès de vitesse est compris entre 30 et 40 km/h
        montant = 135
        point = 3
        suspension = 3
        prison = 0
    elif vitesse - limite >= 40 and vitesse - limite <= 50: #on regarde si l'excès de vitesse est compris entre 40 et 50 km/h
        montant = 135
        point = 4
        suspension = 3
        prison = 0
    elif vitesse - limite >=50: #on regarde si l'excès de vitesse est supérieur ou égal à 50 km/h
        if recidive == True: #on regarde si le conducteur est récidiviste#
            montant = 1500
            point = 6
            suspension = 3
            prison = 3
        else: #le conducteur n'est pas récidiviste
         montant = 1500
         point = 6
         suspension = 3
         prison = 0
    return (montant, point, suspension, prison)



def test_amende():
    assert amende(70, 50, False) == (68, 1, 0, 0)
    assert amende(80, 50, False) == (135, 2, 0, 0)
    assert amende(90, 50, False) == (135, 3, 3, 0)
    assert amende(100, 50, False) == (135, 4, 3, 0)
    assert amende(110, 50, False) == (1500, 6, 3, 0)
    assert amende(120, 50, True) == (1500, 6, 3, 3)