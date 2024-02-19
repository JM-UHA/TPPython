import argparse
import pathlib
import sys


class FindNamespace(argparse.Namespace):
    """Namespace pour les arguments du module find3."""

    d: pathlib.Path
    f: str


def parse_args() -> FindNamespace:
    """Parse les arguments passés en ligne de commande."""
    parser = argparse.ArgumentParser(
        prog="FIND3",
        description="Recherche une occurence de fichier dans un répertoire donné.",
    )
    parser.add_argument("ignore", nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
    parser.add_argument("-d", type=pathlib.Path, help="Le répertoire à analyser.")
    parser.add_argument("-f", type=str, help="Le nom du fichier à rechercher.")
    return parser.parse_args(sys.argv[1:], namespace=FindNamespace())


def recherche(dossier: pathlib.Path, fichier: str):
    """Recherche un fichier dans un répertoire donné."""


def start_find3(args: FindNamespace):
    """Lance la recherche de fichiers dans un répertoire donné."""


if __name__ == "__main__":
    args = parse_args()
    if not args.d:
        print("Le répertoire à analyser n'a pas été spécifié.")
        sys.exit(1)
    if not args.f:
        print("Le fichier à rechercher n'a pas été spécifié.")
        sys.exit(1)
    start_find3(args)
