nombre_etudiants = int(input("Donnez le nombre d'etudiants : "))
somme = 0.0
moyenne = 0.0

notes = []

for i in range(nombre_etudiants):
    note = float(input(f"Note étudiant {i} : "))
    notes.append([i, note])
    somme += note

moyenne = somme / nombre_etudiants
print(f"Moyenne de la classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for etudiant in notes:
    nombre_etudiant = etudiant[0]
    note = etudiant[1]
    ecart = note - moyenne
    print(f"{nombre_etudiant} | {note} | {round(ecart, 1)}")

# Comment vous pouvez faire pour afficher une phrase avec des variables en appelant
# la fonction input() ?

# Nous pouvons faire : input(f"Ma variable : {x}")
