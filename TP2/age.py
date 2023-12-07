from datetime import datetime

annee = int(input("Quel âge avez-vous ? : "))
cette_annee = datetime.now().year

print(f"Votre année de naissance : {cette_annee - annee}")
