# Contenu entre -10 et -2
# Contenu entre 0 (Exclu) et 1
# Contenu entre 2 et 3 (Exclu)

# SEULEMENT < et ==

# -10 <-> -2 /// 0 <-> 1 /// 2 <-> 3
# ___     __           _     _

while True:
    valeur = float(input("Entrez un nombre entier : "))

    if (-10 < valeur < -2) or (valeur == -10) or (valeur == -2):
        print("True")
    elif (0 < valeur < 1) or (valeur == 1):
        print("True")
    elif (2 < valeur < 3) or (valeur == 2):
        print("True")
    else:
        print("False")
