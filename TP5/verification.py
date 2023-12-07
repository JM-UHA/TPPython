import os
from datetime import datetime

first_file = input("Nom du premier fichier : ")
second_file = input("Nom du deuxième fichier : ")

if os.path.isfile(first_file) and os.path.isfile(second_file):
    print(f"Taille du premier fichier : {os.path.getsize(first_file)}")
    print(f"Taille du deuxième fichier : {os.path.getsize(second_file)}")

    t1 = os.path.getmtime(first_file)
    t2 = os.path.getmtime(second_file)

    if t1 > t2:
        print(
            f"Le premier fichier a été modifié en dernier, le {datetime.fromtimestamp(t1)}"
        )
    else:
        print(
            f"Le deuxième fichier a été modifié en dernier, le {datetime.fromtimestamp(t2)}"
        )
