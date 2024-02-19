prenom = "Julien"
nom = "Mauroy"
math = 12
anglais = 16
info = 15
promotion = 2023

print(f"prenom: {type(prenom)}")
print(f"nom: {type(nom)}")
print(f"math: {type(math)}")
print(f"anglais: {type(anglais)}")
print(f"info: {type(info)}")
print(f"promotion: {type(promotion)}")

moyenne = (math + anglais + info) / 3

print(
    f"L'étudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {round(moyenne, 1)}."
)
