# a) Calcul et affichage de la somme des N entiers naturels (de 0 à N inclus) avec N saisit
# par l’utilisateur.

user_input = int(input("Entrez la somme souhaité: "))

total = 0
for i in range(0, user_input + 1):
    total += i
    print(f"On additionne {total - i} et {i}, cela donne {total}")
print(f"Résultat final: {total}")


# b) Boucle d’attente qui se termine si l’utilisateur entre la valeur 100

while int(input("N'entrez surtout pas 100 ! : ")) != 100:
    print("Eheh, je vous ai bien eu !")

# c) Lecture de 10 valeurs réelles comprises entre 0 et 20

valeurs = []
for i in range(10):
    while True:
        obtenu = int(input(f'Ajouter un {len(valeurs) + 1}e nombre : '))
        if not 0 <= obtenu <= 20:
            print("Désolé, cela doit être compris entre 0 et 20 !")
            continue
        break
    valeurs.append(obtenu)

print(f"Nombre de valeurs strictement inférieurs à 10 : {len([i for i in valeurs if i < 10])}")
print(f"Nombre de valeurs contenu entre 10 inclus et 15 exclus : {len([i for i in valeurs if 10 <= i < 15])}")
print(f"Nombre de valeurs supérieur à 15 inclus : {len([i for i in valeurs if i >= 15])}")

# d) Calcul et affichage du plus grand nombre N

X = int(input("Veuillez saisir un nombre X supérieur à 1 : "))

if X <= 1:
    print("Veuillez saisir un nombre supérieur à 1.")
else:
    N = 0
    somme = 0

    while somme <= X:
        N += 1
        somme += N

    resultat = N - 1
    print(f"Le plus grand nombre N tel que ∑(N) <= {X} est {resultat}.")

