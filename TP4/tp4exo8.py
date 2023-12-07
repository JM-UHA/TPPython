data1 = {
    "firstname": "Julien",
    "name": "Mauroy",
    "promo": 2023,
    "group": 131,
}

print(
    f"votre nom est {data1['name']}, prénom est {data1['firstname']}, vous faites partie de la promo {data1['promo']} et votre groupe est {data1['group']}"
)

dic={"name":"toto","firstname":"titi","promo":2022,"group":202}

print("Les clés du dictionnaire sont :")
print("\n".join([f"-{v}" for v in dic.keys()]))
print("Les valeurs du dictionnaire sont :")
print("\n".join([f"-{v}" for v in dic.values()]))
print("Les tuplets du dictionnaire sont :")
print("\n".join([f"-{v}" for v in dic.items()]))

data2 = {
    "firstname": "XXX",
    "name": "YYY",
    "promo": 2023,
    "group": 131,
}

binome = {
    "Poste1": data1,
    "Poste2": data2
}

print("Les étudiants formants le binôme sont :")
for etudiant in binome.values():
    print(f"- L'étudiant {etudiant['firstname']} {etudiant['name']} du groupe {etudiant['group']}")
