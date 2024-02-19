while True:
    entree_brute = input("Entrez un mot ou une phrase : ")

    entree = entree_brute.lower()
    entree = "".join(charactere for charactere in entree if charactere.isalpha())

    entree_inverse = entree[::-1]

    print(
        "C'est un palindrome !"
        if entree == entree_inverse
        else "Ce n'est pas un palindrome."
    )
