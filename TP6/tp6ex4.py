## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs
## comprises entre 'vmin' et 'vmax'


def generer(nbr, vmin, vmax):
    liste = []
    t = -1
    for i in range(vmin, vmax + 1):
        if t >= nbr:
            break
        liste.append(i)
        t += 1
    return liste


## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
## d'un tableau 'table' inférieures à la valeur 'vseuil'


def combienInferieur(table, vseuil):
    t = 0
    for element in table:
        if element < vseuil:
            t += 1
    return t


nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")
