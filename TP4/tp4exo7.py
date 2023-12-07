binome = ("J.M.", "M.F.")

print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")

try:
    binome[1] = "F.V."
except TypeError:
    print("Un tuple est invariable et constant.")

try:
    del binome[1]
except TypeError:
    print("Un tuple est invariable et constant.")

# Vous souhaitez former un trinôme en ajoutant un troisième élément au « tuplet binome ».

# Comment procéder ?
"""
Il faut définir un nouveau tuple.
"""

# Que pouvez-vous en conclure sur les « tuplet » et leurs domaines d’utilisation ?
"""
Les tuples sont invariable. Leurs valeurs ne peuvent être modifié.
Elle sont donc utilisés pour définir des valeurs constantes, qui n'ont pas lieu d'être modifiable.
"""
