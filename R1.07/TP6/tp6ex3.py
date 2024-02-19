# Quel serait le résultat de l’instruction print(ajouter_elt()) ?

# Le résultat serait une liste avec 3 ajouté à sa fin. Ce qui donne :
# [0, 1, 2, 3]

# Répéter l’instruction précédente


def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst


l1 = ajouter_elt()
print(id(l1))
l2 = ajouter_elt()
print(id(l2))

# Qu’est-ce que vous remarquez ?
# >>> La fonction revoie toujours le même objet, car une liste est mutable.

# Déclarer maintenant la fonction ajouter_carac qui prend en paramètres les deux
# arguments ch et elt ayant comme valeur par défaut "abc" et "d" respectivement,
# puis renvoie la concaténation de la chaine ch avec l’élément elt


def ajouter_carac(ch="abc", elt="d"):
    return ch + elt


# Quel serait le résultat de l’instruction print(ajouter_carac())?
# >>> Il serait "abcd"

# Répéter l’instruction précédente

s1 = ajouter_carac()
print(id(s1))
s2 = ajouter_carac()
print(id(s2))

# qu’est-ce que vous remarquez ? pourquoi on a un tel comportement ? Expliquez le résultat obtenu en vous
# aidant de la fonction id()
# >>> Les IDs sont différents, les lignes de caractères sont immutables.
