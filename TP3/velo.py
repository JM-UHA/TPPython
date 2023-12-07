heure_debut = 0
heure_fin = 0
valid = False
while not valid:
    heure_debut = int(input("Entrez l'heure de début de location : "))
    heure_fin = int(input("Entrez l'heure de fin de location : "))

    if heure_debut > 24 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
    elif heure_debut == heure_fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    elif heure_debut > heure_fin:
        print("Attention ! le début de la location est après la fin...\n")
    else:
        valid = True

total_heures = [i for i in range(heure_debut, heure_fin)]

total_heure_soir = len([i for i in total_heures if (0 < i < 7) or (17 <= i < 24)])
total_heure_jour = len([i for i in total_heures if (7 <= i < 17)])

prix_soir = total_heure_soir * 1
prix_jour = total_heure_jour * 2

print("Vous avez loué votre vélo pendant")
if total_heure_soir > 0:
    print(f"{total_heure_soir} heure(s) au tarif horaire de 1.0 euro(s)")
if total_heure_jour > 0:
    print(f"{total_heure_jour} heure(s) au tarif horaire de 2.0 euro(s)")
print(f"Le montant total à payer est de {prix_soir + prix_jour} euro(s).")