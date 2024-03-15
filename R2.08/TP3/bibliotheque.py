import json
import pathlib

from .film import Film


class Bibliothèque:
    def __init__(self, liste_des_films: list[Film]) -> None:
        self._films: list[Film] = liste_des_films

    def __str__(self) -> str:
        return f"Bibliothèque(films={len(self.films)})"

    @property
    def films(self) -> list[Film]:
        return self._films

    def afficher_films(self):
        print(
            "\n\n".join(
                [
                    f"Film {i+1} : {film.titre}\nDate : {film.date_de_sortie}\nNote : {film.note}"
                    f"\nAvis : {', '.join(film.avis)}"
                    for i, film in enumerate(self.films)
                ]
            )
        )

    def mostrate(self):
        return max(self.films, key=lambda film: film.note)

    def top3(self):
        return sorted(self.films, key=lambda film: film.note, reverse=True)[:3]

    def lastmovie(self):
        return max(self.films, key=lambda film: film.date_de_sortie)

    def avrgnote(self):
        return sum([film.note for film in self.films]) / len(self.films)

    def to_json_file(self):
        data = {"films": [film.to_json() for film in self.films]}
        with open("films.json", "w") as file:
            json.dump(data, file)

    @classmethod
    def from_json(cls, file: str | pathlib.Path):
        if isinstance(file, pathlib.Path):
            file = file.resolve()
        with open(file, "r") as movies:
            data = json.load(movies)
            return cls([Film(**film) for film in data["films"]])
