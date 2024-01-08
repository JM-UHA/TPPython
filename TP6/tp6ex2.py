def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst


lst1 = [0, 1, 2]
lst2 = ajouter_elt(lst1, len(lst1))

print(
    f"""=== LST1 ===
type: {type(lst1)}
id: {id(lst1)}
"""
)
print(
    f"""=== LST2 ===
type: {type(lst2)}
id: {id(lst2)}
"""
)

# Qu’est-ce que vous remarquez ?

# >>> L'appel à la fonction a retourné la même liste que nous avons donné.
# Cependant, on pourrait croire qu'on a affaire à une liste différente.
# Les changements que nous effectuerons dans "lst2" seront aussi effectués dans "lst1".
# Il faudrait utiliser copy.copy pour remédier à cela.
