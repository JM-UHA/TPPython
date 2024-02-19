nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

resultat = []
for i in range(10):
    resultat.append(round(nombre * i, 1))

for index, resultat in enumerate(resultat):
    print(f"{nombre} * {index} = {resultat}")
