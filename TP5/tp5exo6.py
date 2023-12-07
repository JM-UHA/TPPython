T1 = ['L', 'e', ' ', 'c', 'i', 'e', 'l', ' ', 'e', 's', 't', ' ', 'b', 'l', 'e', 'u', ',', ' ', 'c', 'o', 'm', 'm', 'e', ' ', 'u', 'n', ' ', 'w', 'a', 'g', 'o', 'n', '.']
T2 = ['W', 'a', 'g', 'o', 'n', ' ', 'a', 'p', 'r', 'è', 's', ' ', 'w', 'a', 'g', 'o', 'n', ',', ' ', 'l', 'e', ' ', 't', 'r', 'a', 'i', 'n', ' ', 'a', 'v', 'a', 'n', 'c', 'e', '.']
T3 = ['I', 'l', ' ', 'y', ' ', 'a', ' ', 'c', 'i', 'n', 'q', ' ', 'w', 'a', 'g', 'o', 'n', 's', ' ', 'd', 'a', 'n', 's', ' ', 'l', 'e', ' ', 't', 'r', 'a', 'i', 'n', '.']
T4 = ['L', 'a', ' ', 'l', 'o', 'c', 'o', 'm', 'o', 't', 'i', 'v', 'e', ' ', 't', 'i', 'r', 'e', ' ', 'l', 'e', 's', ' ', 'w', 'a', 'g', 'o', 'n', 's', '.']
T5 = ['W', 'a', 'g', 'o', 'n', ',', ' ', 'w', 'a', 'g', 'o', 'n', ',', ' ', 'w', 'a', 'g', 'o', 'n', ',', ' ', 'c', 'i', 'e', 'l', ' ', 'b', 'l', 'e', 'u', '.']
T6 = ['L', 'e', ' ', 't', 'r', 'a', 'i', 'n', ' ', 'a', 'v', 'a', 'n', 'c', 'e', ' ', 'a', 'v', 'e', 'c', ' ', 's', 'e', 's', ' ', 'w', 'a', 'g', 'o', 'n', 's', '.']
T7 = ['U', 'n', ' ', 'w', 'a', 'g', 'o', 'n', ' ', 'r', 'o', 'u', 'g', 'e', ' ', 'f', 'i', 'l', 'e', ' ', 'à', ' ', 't', 'o', 'u', 't', 'e', ' ', 'v', 'i', 't', 'e', 's', 's', 'e', '.']
T8 = ['L', 'e', ' ', 'w', 'a', 'g', 'o', 'n', ' ', 'j', 'a', 'u', 'n', 'e', ' ', 't', 'r', 'a', 'n', 's', 'p', 'o', 'r', 't', 'e', ' ', 'd', 'e', 's', ' ', 'm', 'a', 'r', 'c', 'h', 'a', 'n', 'd', 'i', 's', 'e', 's', '.']

ALL = [T1, T2, T3, T4, T5, T6, T7, T8]
VOYELLES = ['a', 'e', 'i', 'o', 'u', 'y']

def reconstructed_str(liste: list):
    return "".join(liste)

for liste in ALL:
    print(f"On va analyser la liste suivante : {reconstructed_str(liste)}.")
    liste = [i.lower() for i in liste]

    # Partie 1
    print("1er partie : Taille de la chaîne de charactère.")
    total = len(liste)
    print(f"Taille : {total}")

    # Partie 2
    print("2e partie : Calcul du pourcentage de voyelle.")
    voyelles = 0
    for character in liste:
        if character in VOYELLES:
            voyelles += 1
    print(f"Pourcentage de voyelles : {round(total / voyelles)}%")

    # Partie 3
    print("3e partie : Test de présence de wagon.")

    reconstruction = ""
    occurence = 0
    detection = 0

    for index, character in enumerate(liste, 1):
        if character == "w":
            reconstruction = "w"
            occurence = index
        else:
            reconstruction += character

        if reconstruction == "wagon":
            print(f"Wagon a été trouvé ! Il est le {occurence}e charactère de la liste.")
            detection += 1

    print("4e partie : Nombre d'occurences de wagon")
    print(f"\"Wagon\" a été trouvé {detection} fois.")

    print("\n")
