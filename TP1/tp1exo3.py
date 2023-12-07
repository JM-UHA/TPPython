jour = int(input("Donnez le nombre de jour qui s'est écoulés : "))
heure = int(input("Donnez le nombre d'heures qui s'est écoulés : "))
minute = int(input("Donnez le nombre de minutes qui se sont écoulés : "))

total = jour * 24 * 60 + heure * 60 + minute

print(f"Il s'est écoulé {total} minutes depuis le 1er du mois.")
