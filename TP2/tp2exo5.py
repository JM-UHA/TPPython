print("Pour sortir de la boucle : Ctrl+C.")
while True:
    nombre = int(input("Entrez un nombre entier : "))
    est_pair = "impair" if bool(nombre % 2) else "pair"

    if nombre == 0:
        print(f"Le nombre est nul, et {est_pair}")
    elif nombre < 0:
        print(f"Le nombre est négatif, et {est_pair}.")
    else:
        print(f"Le nombre est positif, et {est_pair}.")
