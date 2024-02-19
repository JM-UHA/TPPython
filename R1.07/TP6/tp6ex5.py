import re
import unicodedata


def nettoyer_texte(entree: str) -> str:
    return "".join(
        c
        for c in unicodedata.normalize("NFD", entree)
        if unicodedata.category(c) != "Mn"
    )

    # https://stackoverflow.com/a/518232


def est_palindrome(entree_brute: str):
    entree_preface = "".join(
        charactere for charactere in entree_brute.lower() if charactere.isalpha()
    )
    entree = nettoyer_texte(entree_preface.lower())

    entree_inverse = entree[::-1]

    print(
        "C'est un palindrome !"
        if entree == entree_inverse
        else "Ce n'est pas un palindrome."
    )


while True:
    entree = input("Entrez votre texte : ")
    est_palindrome(entree)
