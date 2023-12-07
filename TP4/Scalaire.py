nMax = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

v1 = []
v2 = []

print("Saisie du premier vecteur :")
for i in range(nMax):
    v1.append(int(input(f"v1[{i}] = ")))

print("Saisie du second vecteur :")
for i in range(nMax):
    v2.append(int(input(f"v2[{i}] = ")))

produit_scalaire = 0.0

# On va essayer de ne pas obtenir une complexité de O(n^2)
# https://www.bigocheatsheet.com/

print(v1, v2)

for index, valeur_v1 in enumerate(v1):
    valeur_v2 = v2[index]
    produit_scalaire += valeur_v1 * valeur_v2

print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}")
