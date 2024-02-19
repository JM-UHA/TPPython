"""Module pour l'affichage des fichiers présent dans un répertoire donné en tant qu'argument. """

import sys
import pathlib


def affiche(path: pathlib.Path):
    """Affiche les fichiers et répertoires présents dans le répertoire donné.

    Paramètres
    ----------
    path : pathlib.Path
        Le répertoire à analyser.
    """
    for file_pos, file in enumerate(path.iterdir(), 1):
        print(f"\t{file_pos} => {file.name}")


def start_find1(args: list[str]):
    """Lance le programme principal.

    Ce programme va afficher les fichiers présents dans les répertoires donnés en argument.

    Paramètres
    ----------
    args : list[str]
        Les répertoires à analyser.
    """

    for arg in args:
        path = pathlib.Path(arg)
        if not path.exists():
            print(f"Le répertoire {path.resolve()} n'existe pas.")
            continue
        if not path.is_dir():
            print(f"{path.resolve()} n'est pas un répertoire.")
            continue
        affiche(path)


def aide(executable: str):
    """Affiche l'aide du programme.

    Paramètres
    ----------
    executable : str
        L'exécutable utilisé pour lancer le programme.
    """
    print(f"Usage: python {executable} <répertoire> [<répertoire> ...]")
    print("Affiche les fichiers présents dans les répertoires donnés en argument.")
    print("Si un répertoire n'existe pas, il est ignoré.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) <= 0:
        print("Veuillez donner un répertoire en argument.")
        aide(sys.argv[0])
    else:
        start_find1(args)
