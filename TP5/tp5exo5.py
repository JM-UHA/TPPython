heures = int(input("Combien d'heures de travail ? : "))
salaire_horaire = int(input("Quel est le salaire horaire ? : "))

salaire = 0

salaire_niveau_1 = heures * salaire_horaire
print(f"Salaire de base : {salaire_niveau_1}")

salaire_niveau_2 = max(0.0, (heures - 160) * (salaire_horaire * 1.25))
print(f"Salaire à 25% : {salaire_niveau_2}")

salaire_niveau_3 = max(0.0, (heures - 200) * (salaire_horaire * 1.5))
print(f"Salaire à 50% : {salaire_niveau_3}")

print(f"Salaire total = {salaire_niveau_1 + salaire_niveau_2 + salaire_niveau_3}")
