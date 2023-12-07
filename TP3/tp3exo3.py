import random

valeur_aleatoire = random.randint(0, 100)
nb_tours = 0

entree_utilisateur = None
while entree_utilisateur != valeur_aleatoire:
    entree_utilisateur = int(input("Devinez le nombre entre 0 et 100 : "))
    if entree_utilisateur > valeur_aleatoire:
        print("C'est moins !")
    elif entree_utilisateur < valeur_aleatoire:
        print("C'est plus !")
    nb_tours += 1
print(f"Cela vous a pris {nb_tours} tours pour deviner le nombre {valeur_aleatoire}.")
