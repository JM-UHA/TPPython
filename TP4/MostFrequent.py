L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
"""

# Partie 1

# Initialisation des variables
disponibilite = 0
nombre_frequent = None

# Parcours de la liste
for element in L1:
    # Mise à jour de la fréquence maximale
    freq = 0
    for i in range(len(L1)):
        if L1[i] == element:
            freq += 1
    if freq > disponibilite:
        disponibilite = freq
        nombre_frequent = element

print(
    f"Le nombre le plus frequent dans la liste est le : {nombre_frequent} ({disponibilite} x)"
)

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
*Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
"""
