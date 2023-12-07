# Heureusement que des librairies font ça pour nous...
import sys

while True:
    date_brut = input("Entrez votre date (jjmmaaaa) : ")

    jj = date_brut[:2]
    mm = date_brut[2:4]
    aaaa = date_brut[4:]

    if len(jj) != 2 or len(mm) != 2 or len(aaaa) != 4:
        print("Le format est incorrect !")
        sys.exit(0)

    jj = int(jj)
    mm = int(mm)
    aaaa = int(aaaa)

    if mm in (1, 3, 5, 7, 8, 10, 12):
        jours_max = 31
    elif mm in (4, 6, 9, 11):
        jours_max = 30
    elif (aaaa % 400 == 0) or ((aaaa % 4 == 0) and (aaaa % 100 != 0)):
        jours_max = 29
    else:
        jours_max = 28

    if jj <= 0:
        print("Un jour ne peut pas être égal ou inférieur à 0.")
    elif mm <= 0:
        print("Un mois ne peut pas être égal ou inférieur à 0.")
    elif jj > jours_max:
        print(f"Votre valeur des jours est trop grande ! (Max. {jours_max})")
    elif mm > 12:
        print("Votre valeur des mois est trop grande ! (Max. 12)")
    else:
        print("C'est correct !")
