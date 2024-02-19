# Initialisez une liste ne comprenant que trois zéros à l’aide de la commande Python « L1
# = [0]*3 » qui concatène trois listes à élément unique «[0]» en une seule et affichez
# la liste obtenue ainsi que son type et son id.

L1 = [0] * 3

print(L1)
# >>> [0, 0, 0]
print(f"type: {type(L1)}")
# >>> <class 'list'>
print(f"id: {id(L1)}")
# >>> 2921788069952

# Pour chaque élément de la liste précédente, affichez sa valeur, son type et son
# identifiant à l’aide des fonctions «type()» et «id()». Qu’est-ce que vous
# remarquez ?
for index, element in enumerate(L1):
    print(f"Pour l'élément {index}: {element}")
    print(f"type: {type(element)}")
    print(f"id: {id(element)}")
    # Qu’est-ce que vous remarquez ?
    # >>> Chacun de ces éléments ont le même ID, ce qui indique qu'ils sont les mêmes objets pour Python.


# Modifiez l’élément en deuxième position en rajoutant 1 à sa valeur puis affichez de
# nouveau la liste ainsi que son type et son id.

L1[1] = 1
print(f"id: {id(L1)}")
# Est-ce que l’id de la liste à changer ?
# >>> L'ID de la liste n'a pas changé.

# Revérifier les identifiants de chaque élément de la liste, est-ce que c’est un nouvel objet
# qui a été créé suite à l’incrémentation ou bien c’est toujours le même ? que pouvez-vous
# en conclure sur les éléments de la liste
for index, element in enumerate(L1):
    print(f"Pour l'élément {index}: {element}")
    print(f"type: {type(element)}")
    print(f"id: {id(element)}")
    # L'élément à l'index "1" (Commençat à 0) n'a plus le même ID que les autres éléments de la liste.
    # Il est donc un nouvel objet sans aucun lien avec les autres objets de la liste.

# Déclarer une variable avec la chaine "machaine" puis faite le même test en affichant
# l’identifiant de la variable et le type et l’identifiant de chaque caractère de la chaine.
my_str = "machaine"
print(f"my_str id: {id(my_str)}")
L1[2] = my_str
print(f"my_str id in list: {id(L1[2])}")
# Qu’est-ce que vous remarquez ?
# >>> L'ID de la variable est de la liste est le même. Ce sont les même objets.
