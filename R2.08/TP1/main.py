class Voiture:
    _couleur: str
    
    _marque: str
    
    _modele: str
    
    _puissance: int
    
    _options: list[str]
    
    def __init__(self, couleur: str = "Rouge", marque: str = "Mercedes", modele: str = "Classe 1", puissance: int = 0) -> None:
        self._couleur = couleur
        self._marque = marque
        self._modele = modele
        self._puissance = puissance
        self._options = []

    def __str__(self) -> str:
        return (
            f"Voici les caractéristiques de la voiture:\n- Couleur : {self.couleur}"
            f"\n- Modele : {self.modele}\n- Marque : {self.marque}\n"
            f"- Puissance : {self.puissance}\n"
            f"- Options : {', '.join(self._options) or 'Aucune'}"
        )

    @property
    def couleur(self) -> str:
        return self._couleur
    
    @couleur.setter
    def couleur(self, couleur: str) -> None:
        self._couleur = couleur
    
    @property
    def marque(self) -> str:
        return self._marque
    
    @marque.setter
    def marque(self, marque: str) -> None:
        self._marque = marque
    
    @property
    def modele(self) -> str:
        return self._modele
    
    @modele.setter
    def modele(self, modele: str) -> None:
        self._modele = modele
    
    @property
    def puissance(self) -> int:
        return self._puissance
    
    @puissance.setter
    def puissance(self, puissance: int) -> None:
        self._puissance = puissance

    @property
    def options(self) -> list[str]:
        return self._options
    
    @options.setter
    def options(self, options: list[str]) -> None:
        self._options = options
        
    def ajouter_option(self, option: str) -> None:
        if option not in self.options:
            self._options.append(option)
        
    def retirer_option(self, option: str) -> None:
        if option in self.options:
            self._options.remove(option)

    def is_option_present(self, option: str) -> bool:
        return option in self.options

mycar1 = Voiture("rouge")
print(vars(mycar1))

mycar2 = Voiture()
print(vars(mycar2))

mycar3 = Voiture("Rouge", "Renault", "Classe 3")
print(vars(mycar3))

mycar4 = Voiture(couleur="Chrome")
print(vars(mycar4))

# Partie 2
# Question 5. ⛔
# Transformer les attributs publics en privés et observer qu’il est impossible d’y accéder en
# dehors de la classe Voiture

# Ceci est faux. Il est possible d'accéder aux attributes privés d'une instance.
# Cette écriture (Avec un tiret du bas devant l'attribut) est une convention pour dire que
# l'attribut est privé.
# Elle n'est cependant, pas une règle de syntaxe.
# Il serait donc possible d'accéder à l'attribut privé en dehors de la classe.

mycar1.couleur = "Bleu"

mycar2.marque = "BMW"

print(vars(mycar1))
print(vars(mycar2))

print(mycar1)

# Tests pour options

mycar1.ajouter_option("Climatisation")
assert mycar1.is_option_present("Climatisation")
assert not mycar1.is_option_present("GPS")
mycar1.ajouter_option("GPS")
assert mycar1.is_option_present("GPS")
mycar1.retirer_option("Climatisation")
assert not mycar1.is_option_present("Climatisation")
print("Tests OK (normalement...)")
