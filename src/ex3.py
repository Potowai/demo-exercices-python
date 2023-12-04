print("Calcul de l'aire et du perimetre d'un quadrilatere")
longueur = (int(input("Quelle est la longueur?\n")))
largeur = (int(input("Quelle est la largeur\n")))


def calc_aire():
    return largeur * longueur


def calc_perimetre():
    return (largeur * 2) + (longueur * 2)


if (largeur != 0 and longueur != 0):
    print("L'aire :", calc_aire())
    print("Le perimetre :", calc_perimetre())
    print("Carré de ", longueur, "x", largeur, " :")
    for i in range(0, largeur + 1):
        print("-" * longueur)
else:
    print("ERROR : Longueur ou largeur = 0 !")
