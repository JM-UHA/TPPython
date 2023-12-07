import sys

method = input("Quel méthode souhaitez vous utiliser ? (for, while) : ")

if method not in ("for", "while"):
    sys.exit(0)

number = int(input("Entrez votre nombre : "))
if number < 0:
    print("Le nombre doit être supérieur à 0 !")
    sys.exit(0)


# Méthode "for"
if method == "for":
    resultat = 1

    if number != 0:
        for i in range(1, number + 1):
            resultat *= i

    print(resultat)

# Méthode "while"
elif method == "while":
    resultat = 1
    i = 1
    if number != 0:
        while number >= i:
            resultat *= i
            i += 1
    print(resultat)
