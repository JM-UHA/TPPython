valeur_totale = int(input("Quel est la valeur totale ? : "))

restant = valeur_totale

# Billets de 100
b100 = int(restant / 100)
restant = restant % 100

# Billets de 50
b50 = int(restant / 50)
restant = restant % 50

# Billets de 10
b10 = int(restant / 10)
restant = restant % 10

# Pièces de 2
p2 = int(restant / 2)
restant = restant % 2

# Pièces de 1
p1 = int(restant / 1)
restant = restant % 1

print(
    f"{valeur_totale} euros, c’est donc {b100} billets de 100, {b50} de 50, {b10} de 10, {p2} pièces de 2 et {p1} pièce 1."
)
