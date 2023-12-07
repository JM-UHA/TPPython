moyenne = 0
notes = []
coefficients = 0

for i in range(1, 6):
    valeur_brut = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")

    note, coefficient = valeur_brut.split()
    note = float(note)
    coefficient = int(coefficient)

    notes.append(note)
    coefficients += coefficient
    moyenne += note * coefficient

print(f"La moyenne est de {round(moyenne / coefficients, 1)}")

if any(note < 8 for note in notes) or moyenne < 10:
    print("L'étudiant n'est pas admissible.")
else:
    print("L'étudiant est admissible.")
