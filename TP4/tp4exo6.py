tab = [
    [5, 2, 4, 8, 1, 3],
    [1, 2, 4, 8, 5, 3],
    [1, 2, 4, 8, 5, 3],
    [1, 2, 3, 8, 5, 4],
    [1, 2, 3, 4, 5, 8],
    [1, 2, 3, 4, 5, 8],
]

print(sorted(tab))
# qu’est-ce que vous remarquez ?
"""
La liste tab n'est pas alteré, une nouvelle variable est comme créé.
De plus, toutes les sous-listes ne sont pas trié comme la première sous-liste.

C'est parce que Python va trier les sous-listes, mais pas les valeurs des sous-listes.
"""

tab.sort()
print(tab)
"""
La liste est alteré, et on se retrouve avec le même résultat.
"""
