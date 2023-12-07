import time

print("Méthode \"for\".")

entree = 0
while entree <= 0:
    entree = int(input("Entrez le temps d'attente : "))

for i in range(entree):
    print(f"On attend encore {entree - i} secondes...")
    time.sleep(1)

print("Méthode \"while\".")

entree = 0
while entree <= 0:
    entree = int(input("Entrez le temps d'attente : "))

while entree >= 1:
    print(f"On attend encore {entree} secondes...")
    time.sleep(1)
    entree -= 1

